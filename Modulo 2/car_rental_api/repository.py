class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager


    def _format_user(self, user):
        return{
            "id": user[0],
            "full_name": user[1],
            "email": user[2],
            "username": user[3],
            "password": user [4],
            "birth_date": str(user [5]),
            "account_status": user[6],
            "is_delinquent": user[7],

        }
    
    def get_all(self, filters=None):
            query = """
                SELECT id, full_name, email, username, password, birth_date, account_status, is_delinquent
                FROM lyfter_car_rental.users
            """

            params = []

            if filters:
                conditions = []

                for column, value in filters.items():
                    conditions.append(f"{column} = %s")
                    params.append(value)

                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(query, tuple(params))

            return [self._format_user(user) for user in results]
    
    def create(
        self,
        full_name,
        email,
        username,
        password,
        birth_date,
        account_status="active"
    ):
        
        query = """
            INSERT INTO lyfter_car_rental.users
            (
                full_name,
                email,
                username,
                password,
                birth_date,
                account_status
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id;
        """

        result = self.db_manager.execute_query(
            query,
            (
                full_name,
                email,
                username,
                password,
                birth_date,
                account_status
            )
        )

        return result[0][0]
    
    def flag_delinquent(self, user_id):
        query = """
            UPDATE lyfter_car_rental.users
            SET is_delinquent = TRUE
            Where id = %s;
        """

        self.db_manager.execute_query(query, (user_id,))

        return True
    
    def update_status(self, user_id, account_status):
        query = """
            UPDATE lyfter_car_rental.users
            SET account_status = %s
            WHERE id = %s
        """

        self.db_manager.execute_query(
            query,
            (account_status, user_id)
        )

        return True

    
class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car):
        return {
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "manufacturing_year": car[3],
            "car_status": car[4],
        }    
    
    def get_all(self, filters=None):
        query = """
            SELECT id, brand, model, manufacturing_year, car_status
            FROM lyfter_car_rental.cars
        """

        params = []

        if filters:
            conditions = []

            for column, value in filters.items():
                conditions.append(f"{column} = %s")
                params.append(value)

            query += " WHERE " + " AND ".join(conditions)

        results = self.db_manager.execute_query(query, tuple(params))

        return [self._format_car(car) for car in results]
    
    def create(
        self,
        brand,
        model,
        manufacturing_year,
        car_status="available"
    ):
        
        query = """
            INSERT INTO lyfter_car_rental.cars
            (
                brand,
                model,
                manufacturing_year,
                car_status           
            )
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """

        result = self.db_manager.execute_query(
            query,
            (
                brand,
                model,
                manufacturing_year,
                car_status
            )
        )

        return result[0][0]
    
    def update_status(self, car_id, car_status):
        query = """
            UPDATE lyfter_car_rental.cars
            SET car_status = %s
            WHERE id = %s;
        """

        self.db_manager.execute_query(
            query,
            (car_status, car_id)
        )

        return True
    

class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rental(self, rental):
        return {
            "id": rental[0],
            "user_id": rental[1],
            "car_id": rental[2],
            "rental_date": str(rental[3]),
            "returning_date": str(rental[4]),
            "rental_status": rental[5],
        }
    
    def get_all(self, filters=None):
        query = """
            SELECT id, user_id, car_id, rental_date, returning_date, rental_status
            FROM lyfter_car_rental.rentals
        """

        params = []

        if filters:
            conditions = []

            for column, value in filters.items():
                conditions.append(f"{column} = %s")
                params.append(value)

            query += " WHERE " + " AND ".join(conditions)

        results = self.db_manager.execute_query(query, tuple(params))        

        return [self._format_rental(rental) for rental in results]
    
    def create(
        self,
        user_id,
        car_id,
        returning_date,
        rental_status="active"
    ):
        query = """
            INSERT INTO lyfter_car_rental.rentals
            (
                user_id,
                car_id,
                returning_date,
                rental_status
            )
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """

        result = self.db_manager.execute_query(
            query,
            (
                user_id,
                car_id,
                returning_date,
                rental_status
            )
        )

        return result[0][0]
    
    def update_status(self, rental_id, rental_status):
        query = """
            UPDATE lyfter_car_rental.rentals
            SET rental_status = %s
            WHERE id = %s;
        """

        self.db_manager.execute_query(
            query,
            (rental_status, rental_id)
        )

        return True
    
    def complete_rental(self, rental_id):
        rental_result = self.db_manager.execute_query(
            """
            SELECT car_id
            FROM lyfter_car_rental.rentals
            WHERE id = %s;
            """,
            (rental_id,)
        )

        if not rental_result:
            return False

        car_id = rental_result[0][0]

        update_rental_query = """
            UPDATE lyfter_car_rental.rentals
            SET rental_status = 'completed'
            WHERE id = %s;
        """

        update_car_query = """
            UPDATE lyfter_car_rental.cars
            SET car_status = 'available'
            WHERE id = %s;
        """

        return self.db_manager.execute_transaction([
            (update_rental_query, (rental_id)),
            (update_car_query, (car_id))
        ])