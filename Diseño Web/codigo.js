
dineroCofla = prompt("Cuánto dinero tienes Cofla?");


if (dineroCofla >= 0.6 && dineroCofla < 1) {
	alert("comprate el helado de agua");
}
else if (dineroCofla >= 1 && dineroCofla < 1.6) {
	alert("comprate el helado de crema ");
}
else if (dineroCofla >= 1.6 && dineroCofla < 1.7) {
	alert("comprate el helado marca heladix ");
}
else if (dineroCofla >= 1.7 && dineroCofla < 1.8) {
	alert("comprate el helado marca heladivich ");
}
else if (dineroCofla >= 1.8 && dineroCofla < 2.9) {
	alert("comprate el helado marca helardo ");
}
else if (dineroCofla >= 2.9) {
	alert("comprate el helado con confite o el pote de un 1/4");

}else{
	alert("Lo siento no te alcanza para ningun helado");
}

