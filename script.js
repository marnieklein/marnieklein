
// Back to top button
document.addEventListener("DOMContentLoaded", function() {console.log("true") ;
    document.getElementById("BackToTopButton").addEventListener("click", function() {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
});

