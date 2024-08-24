export interface Employee {
  title: string;
  firstName: string;
  lastName: string;
  imagePath: string;
  phone: string;
  mail: string;
}

export const employees: Employee[] = [
  {
    title: "Leitung Triage und Pflegefachperson",
    firstName: "Ulrich",
    lastName: "Bieri",
    imagePath: "/employees/triage-1.jpg",
    phone: "+41 44 931 39 00",
    mail: "ub@clienia.ch",
  },
  {
    title: "Stv. Leitung Triage und Pflegefachperson",
    firstName: "Simone",
    lastName: "Meier",
    imagePath: "/employees/triage-2.jpg",
    phone: "+41 71 987 63 00",
    mail: "sm@clienia.ch",
  },
  {
    title: "Triageverantwortlicher",
    firstName: "Christian",
    lastName: "Erhard",
    imagePath: "/employees/triage-3.jpg",
    phone: "+41719391121",
    mail: "ce@clienia.ch",
  },
  {
    title: "Triageverantwortlicher",
    firstName: "Marius",
    lastName: "Peter",
    imagePath: "/employees/triage-4.jpg",
    phone: "+41 79 352 93 27",
    mail: "mp@clienia.ch",
  },
  {
    title: "Pflegefachperson",
    firstName: "Ramona",
    lastName: "Junker",
    imagePath: "/employees/triage-5.jpg",
    phone: "+41719997266",
    mail: "rj@clienia.ch",
  },
  {
    title: "Pflegefachperson",
    firstName: "Ida",
    lastName: "Pauli",
    imagePath: "/employees/triage-6.jpg",
    phone: "+41 79 892 94 52",
    mail: "ip@clienia.ch",
  },
];
