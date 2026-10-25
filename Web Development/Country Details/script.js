window.addEventListener("keydown", function(event){
    if (event.key=="Enter"){
        const country=document.getElementById("cname").value;
        document.getElementById("error").textContent="";
        if (country==""){
            document.getElementById("error").textContent="Please enter the name!";
            document.getElementById("country").textContent="Country : Not Entered";
            document.querySelectorAll(".ans").forEach(element => {
                element.textContent="";
            });
            document.getElementById("flag").src="img.png";
        }
        else{
            document.getElementById("load").style.display="inline";
            getdata(country)
        }
        
        
    }
})

async function getdata(country){
    const response= await fetch(`https://api.restcountries.com/countries/v5/names.common/${country}`,{
        "headers":{"Authorization":"Bearer rc_live_11de6e8e385544daaa4fc2f51aab9bde"}
    })
    const value=await response.json();
    document.getElementById("load").style.display="none";
    details=value.data.objects;
    if (details.length===0){
        document.getElementById("error").textContent="The country name is spelt wrong or doesn't exist!";
        document.getElementById("country").textContent="Country : Not Entered";
        document.querySelectorAll(".ans").forEach(element => {
            element.textContent="";
        });
        document.getElementById("flag").src="img.png";

    }
    else{
        const capitals=details[0]["capitals"].map(item=>item.name);
        const currency=details[0]["currencies"].map(item=>item.name+"("+item.symbol+")");
        var brdr=details[0]["borders"].join(", ");
        if (brdr.length==0){
            brdr="No bordering countries"
        }
        document.getElementById("flag").src=details[0]["flag"]["url_png"];
        document.getElementById("error").textContent="";
        document.getElementById("name").textContent=details[0]["names"]["common"];
        document.getElementById("country").textContent="Country  : "+details[0]["names"]["common"];
        document.getElementById("cc").textContent=capitals.join(", ");
        document.getElementById("cont").textContent=details[0]["continents"];
        document.getElementById("sr").textContent=details[0]["subregion"];
        document.getElementById("gov").textContent=details[0]["government_type"];
        document.getElementById("cur").textContent=currency.join(", ");
        document.getElementById("ar").textContent=details[0]["area"]["kilometers"]+"sq.km /"+details[0]["area"]["miles"]+"sq.miles";
        document.getElementById("pop").textContent=details[0]["population"];
        document.getElementById("border").textContent=brdr;
        document.getElementById("tz").textContent=details[0]["timezones"].join(", ");
        console.log(details[0]);
    }
}
document.getElementById("submit").addEventListener("click", function(event){
        const country=document.getElementById("cname").value;
        document.getElementById("error").textContent="";
        if (country==""){
            document.getElementById("error").textContent="Please enter the name!";
            document.getElementById("country").textContent="Country : Not Entered"
            document.querySelectorAll(".ans").forEach(element => {
                element.textContent="";
            });
            document.getElementById("flag").src="img.png";
        }
        else{
            document.getElementById("load").style.display="inline";
            getdata(country)
        }
    })