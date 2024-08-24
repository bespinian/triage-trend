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
		title: "Facharzt für Psychiatrie und Psychotherapie",
		firstName: "Volker",
		lastName: "Böckmann",
		imagePath: "/employees/boeckmann.png",
		phone: "+41 44 931 39 39",
		mail: "volker.boeckmann@clienia.ch"
	},
	{
		title: "Oberpsychologin",
		firstName: "Melanie",
		lastName: "Achermann",
		imagePath: "/employees/achermann.png",
		phone: "+41 71 929 63 44",
		mail: "melanie.achermann@clienia.ch"
	},
	{
		title: "Oberarzt",
		firstName: "Visar",
		lastName: "Beqiri",
		imagePath: "/employees/beqiri.png",
		phone: "+41719296320",
		mail: "visar.beqiri@clienia.ch"
	},
	{
		title: "Oberarzt",
		firstName: "Tobias",
		lastName: "Blechinger",
		imagePath: "/employees/blechinger.png",
		phone: "",
		mail: "tobias.blechinger@clienia.ch"
	},
	{
		title: "Oberpsychologin",
		firstName: "Annina",
		lastName: "Bieri",
		imagePath: "/employees/bieri.png",
		phone: "+41719296823",
		mail: "annina.bieri@clienia.ch"
	},
	{
		title: "Oberpsychologe (DE)",
		firstName: "Christoph",
		lastName: "Christiansen",
		imagePath: "/employees/christiansen.png",
		phone: "+41 71 929 63 41",
		mail: "christoph.christiansen@clienia.ch"
	},
	{
		title: "Oberärztin",
		firstName: "Daliborka",
		lastName: "Djordjevic",
		imagePath: "/employees/djordjevic.png",
		phone: "",
		mail: "daliborka.djordjevic@clienia.ch"
	}
];
