console.log("HELLO!")

document.addEventListener("DOMContentLoaded", async () => {
const card = document.getElementById("template")
const parent = document.getElementById("server-list")
    const status = await (await fetch("https://raw.githubusercontent.com/easysst/easysst.github.io/main/configs/out.json")).json()
    const eg = status.epicgames
    
    for (const [key, value] of Object.entries(eg.targets)){
        console.log(value)
        addCard(value.name, value.status)
    }



    function addCard(name, status, icon){
        clone = card.cloneNode(true)

        clone.getElementsByTagName("h3")[0].innerHTML = name
        statusElement = clone.getElementsByTagName("p")[0]
        statusElement.classList.add(status ? "text-green-500" :"text-red-500")
        statusElement.innerHTML = status ? "Online" : "Offline"
        clone.getElementsByTagName("img")[0].setAttribute("src", icon)
        
        clone.classList.remove("hidden")
        parent.appendChild(clone)
    }
})
