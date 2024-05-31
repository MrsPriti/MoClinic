
var patients = [
    { id: "001", name: "Ajay Kumar Rout", age: 45, bloodPressure: "120/80", symptoms: "Fever, Cough", address: "123 Main St, City, Country" },
    { id: "002", name: "Subrat Nayak", age: 29, bloodPressure: "130/85", symptoms: "Headache, Nausea", address: "456 Park Ave, Town, Country" },
    { id: "003", name: "Jyoti Mohapatra", age: 37, bloodPressure: "140/90", symptoms: "Chest Pain", address: "789 Oak St, Village, Country" },
    { id: "004", name: "Aditya Das", age: 23, bloodPressure: "110/70", symptoms: "Fatigue, Dizziness", address: "101 Pine St, Hamlet, Country" }
];

var currentIndex = 0;

function showNextPatient() {
    currentIndex = (currentIndex + 1) % patients.length;
    var patient = patients[currentIndex];
    document.getElementById("patientId").textContent = patient.id;
    document.getElementById("patientName").textContent = patient.name;
    document.getElementById("patientAge").textContent = patient.age;
    document.getElementById("patientBloodPressure").textContent = patient.bloodPressure;
    document.getElementById("patientSymptoms").textContent = patient.symptoms;
    document.getElementById("patientAddress").textContent = patient.address;
}
