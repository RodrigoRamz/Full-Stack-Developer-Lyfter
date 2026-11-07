const student = {
    name: "John Doe",
    grades: [
        { name: "math", grade: 80 },
        { name: "science", grade: 100 },
        { name: "history", grade: 60 },
        { name: "PE", grade: 90 },
        { name: "music", grade: 98 }
    ]
};

let total = 0;

for (let i = 0; i < student.grades.length; i++) {
    total += student.grades[i].grade;
}

const average = total / student.grades.length;
console.log("Average:", average);

let highest = student.grades[0];
let lowest = student.grades[0];

for (let i = 1; i < student.grades.length; i++) {
    const current = student.grades[i];

    if (current.grade > highest.grade) {
        highest = current;
    }
}

for (let i = 1; i < student.grades.length; i++) {
    const current = student.grades[i];

    if (current.grade < lowest.grade) {
        lowest = current;
    }
}

const result = {
    name: student.name,
    gradeAvg: average,
    highestGrade: highest.name,
    lowestGrade: lowest.name
};

console.log(result);

console.log(total);