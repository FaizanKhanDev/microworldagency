// navbar Functions ///

// mouse Enter in navbar ///

const mainheader = document.querySelector(".mainheader");
const NavAllItems = document.querySelectorAll(".allNavItems");

    mainheader.addEventListener("mouseenter", () => {
      mainheader.classList.add("primary-bg-white");
      for (var k = 0; k < NavAllItems.length; k++) {
        allNavItems[k].style.color = "#000";
      }

  });
// mouse leave in navbar ///

mainheader.addEventListener("mouseleave", ()=> {
  mainheader.classList.remove("primary-bg-white");
  for (var l = 0; l < NavAllItems.length; l++) {
    allNavItems[l].style.color = "#fff";
  }
});

const navLinks = document.querySelectorAll('.allNavItems a');
const currentPath = window.location.pathname;

navLinks.forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('ouractivemenu');
  }
});
// navbar Functions ///


// On Window Scroll ///

const navbar = document.getElementById("navbar");
const headers = document.getElementById("header");
const navBarlogo = document.getElementById("logo");
const allNavItems = document.querySelectorAll(".allNavItems");


window.onscroll = function ()  {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 20 ) {
        navbar.style.backgroundColor = "#fff";
        for (var i = 0; i < allNavItems.length; i++){
          allNavItems[i].style.color = "#000";
        }
        navbar.style.top = "0";
        navbar.style.color = "#000";
        headers.style.display = "none";
        navBarlogo.style.color = "#000";

        mainheader.addEventListener("mouseleave", ()=> {
          mainheader.classList.remove("primary-bg-white");
          for (var l = 0; l < NavAllItems.length; l++) {
            allNavItems[l].style.color = "#000";
          }
        });
        
        

    }
    else {
        navbar.style.backgroundColor = "transparent";
        navbar.style.top = "40px";
        headers.style.display = "flex";
        for(var j = 0; j < allNavItems.length; j++){
          allNavItems[j].style.color = "#fff"
        }
        navBarlogo.style.color = "#fff";
        mainheader.addEventListener("mouseleave", ()=> {
          mainheader.classList.remove("primary-bg-white");
          for (var l = 0; l < NavAllItems.length; l++) {
            allNavItems[l].style.color = "#fff";
          }
        });

    }
};

////// hamburger Menu /////
  function change(bar) {
    bar.classList.toggle("change")
  };

// //// hamburger Menu /////

// /// Start Project Btn ////
const getstarted = document.getElementById("get-started-con");
const topheader = document.getElementById("topheader");

  function startproject () {
    getstarted.style.right = "0px";
    if (getstarted.style.right == "0px") {

    }
  };
  function closestartProject() {
    getstarted.style.right = "-1500px";





  };

// /// Start Project Btn ////


function CloseDrop() {
  var menu = document.getElementById("dropMenu");
  menu.style.display = "none";
  var openDrop = document.getElementById("openDrop");
  var CloseDrop = document.getElementById("CloseDrop");
  CloseDrop.style.display = "none";
  openDrop.style.display = "block";

}
function openDrop() {
  var menu = document.getElementById("dropMenu");
  var openDrop = document.getElementById("openDrop");
  openDrop.style.display = "none";
  menu.style.display = "block";
  var CloseDrop = document.getElementById("CloseDrop");
  CloseDrop.style.display = "block";



}









console.log(window.screen.width);
        // var screenWidth = window.innerWidth;
        // document.write("Screen Width: " + screenWidth + " pixels");

    



function category(categor) {
  categor.classList.toggle("change")
} 






// document.addEventListener("contextmenu", function(event) {
//   event.preventDefault();
// });



