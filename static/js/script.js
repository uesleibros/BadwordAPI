if(localStorage.getItem("mode") == null) { // Se o usuário entrou no site pela primeira vez:
  localStorage.setItem("mode", "white") // O modo vai para (white/branco)
  localStorage.setItem("icon", "https://www.iconpacks.net/icons/2/free-sun-icon-3337-thumb.png")
  document.querySelector("#mode").src = localStorage.getItem("icon")
}

function getMode(){
  return localStorage.getItem("mode")
}

if (getMode() == 'white') {
  document.querySelector("#toggle").checked = false
} else {
  document.querySelector("#toggle").checked = true
}

function madeChanges(){
  document.querySelector("#mode").src = localStorage.getItem("icon")

  if (getMode() == "dark") {
    document.body.style.backgroundColor = "#292929"
    document.querySelectorAll('p').forEach(e => e.style.color = "white");
    document.querySelectorAll('h3').forEach(e => e.style.color = "white");
    document.querySelectorAll('h1').forEach(e => e.style.color = "white");
    document.querySelectorAll('li').forEach(e => e.style.color = "white");
    document.querySelectorAll('span').forEach(e => e.style.color = "white");
    document.querySelectorAll(".container").forEach(c => c.style.backgroundColor = "#131313");
    // TRANSIÇÃO
    document.body.style.transition = "all 1s"
    document.querySelectorAll('p').forEach(e => e.transition = "all 1s");
    document.querySelectorAll('h3').forEach(e => e.transition = "all 1s");
    document.querySelectorAll('h1').forEach(e => e.transition = "all 1s");
    document.querySelectorAll('li').forEach(e => e.transition = "all 1s");
    document.querySelectorAll('span').forEach(e => e.transition = "all 1s");
    document.querySelectorAll(".container").forEach(c => c.style.transition = "all 1s");
  } else {
    document.body.style.backgroundColor = "white"
    document.querySelectorAll('p').forEach(e => e.style.color = "#292929");
    document.querySelectorAll('h3').forEach(e => e.style.color = "#292929");
    document.querySelectorAll('h1').forEach(e => e.style.color = "#292929");
    document.querySelectorAll('li').forEach(e => e.style.color = "#292929");
    document.querySelectorAll(".container").forEach(c => c.style.backgroundColor = "white");
    document.querySelectorAll("span").forEach(e => e.style.color = "#292929");
  }
  
}

function turn() {
  if (getMode() == "white") {
    localStorage.setItem("mode", "dark") // O modo vai para (dark/escuro)
    localStorage.setItem("icon", "https://images-ext-2.discordapp.net/external/mRykDXjwapTE6BDe_GqY_HskC0E_mo5_xDcnM5D78p4/https/www.iconsdb.com/icons/preview/white/moon-4-xxl.png?width=230&height=230")
    
  } else {
    localStorage.setItem("mode", "white") // O modo vai para (white/branco)
    localStorage.setItem("icon", "https://www.iconpacks.net/icons/2/free-sun-icon-3337-thumb.png")
  }
  madeChanges()
}
      
madeChanges(); // Aplica o tema ao abrir o site
