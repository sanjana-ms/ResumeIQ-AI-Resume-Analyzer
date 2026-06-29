const resumeInput = document.getElementById("resume");
const fileName = document.getElementById("file-name");

if (resumeInput) {

    resumeInput.addEventListener("change", function () {

        if (this.files.length > 0) {

            fileName.innerHTML = "✅ " + this.files[0].name;

            fileName.style.color = "#16a34a";

        } else {

            fileName.innerHTML = "No file selected";

            fileName.style.color = "#2563eb";

        }

    });

}
const form = document.querySelector("form");

const loading = document.getElementById("loading");

if(form){

form.addEventListener("submit",function(){

loading.style.display="block";

document.getElementById("analyzeBtn").disabled=true;

});

}