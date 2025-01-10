document.getElementById("love-form").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const yourName = document.getElementById("your-name").value.trim();
    const partnerName = document.getElementById("partner-name").value.trim();
    const resultDiv = document.getElementById("result");
    const scoreSpan = document.getElementById("score");
  
    if (yourName === "" || partnerName === "") {
      alert("Please fill in both names!");
      return;
    }
  
    // Generate a random love score between 50 and 100
    const loveScore = Math.floor(Math.random() * 51) + 50;
  
    scoreSpan.textContent = loveScore;
    resultDiv.classList.remove("hidden");
  });
  