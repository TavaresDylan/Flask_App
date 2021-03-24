const list = document.getElementById("list")
const btn = document.getElementById("btn")

function updateContact(){
    if (btn.value == "Afficher les contacts"){
        axios.get("https://jsonplaceholder.typicode.com/users").then(response => {
            response.data.forEach(element => {
                console.log(element)
                website = "<a href=\"https://"+element.website+"\">"+element.website+"</a>"
                list.innerHTML += "<li>"+element.name+" - "+element.email+"<br/><img src=\"https://img.icons8.com/metro/22/000000/phone-disconnected.png\"/> "+element.phone+"<br/>"+website+"<br/><img src=\"https://img.icons8.com/android/24/000000/marker.png\"/>"+element.address.street+", "+element.address.city+" "+element.address.zipcode+"</li><br/><br/>"
            });
        })
        .catch(function (error) {
            console.log(error);
        })
        .then(function () {
            // always executed
        }); 
        btn.value = "Cacher les contacts"
    }
    else if (btn.value == "Cacher les contacts"){
        list.innerHTML = ""
        btn.value = "Afficher les contacts"
    }
}