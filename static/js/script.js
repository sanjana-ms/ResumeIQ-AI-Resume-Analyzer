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
const loadingText = document.getElementById("loading-text");
const analyzeBtn = document.getElementById("analyzeBtn");

if (form) {

    form.addEventListener("submit", function () {

        loading.style.display = "block";

        if (analyzeBtn) {
            analyzeBtn.disabled = true;
        }

        const messages = [
            "📤 Uploading Resume...",
            "📄 Reading Resume...",
            "🤖 Matching Skills...",
            "📊 Calculating ATS Score...",
            "✅ Preparing Report..."
        ];

        let index = 0;

        loadingText.innerHTML = messages[index];

        setInterval(function () {

            index++;

            if (index < messages.length) {

                loadingText.innerHTML = messages[index];

            }

        }, 1200);

    });

}