
function onClickedPredictSentiment() {
  console.log("Predict sentiment button clicked");
  var Review = document.getElementById("uiSqft");
  var pdSentiment = document.getElementById("uiPredictSentiment");

  var url = "http://127.0.0.1:5000/predict_sentiment"; 
  $.post(url, {
      review: Review.value
  },function(data, status) {
      console.log(data.predicted_sentiment);
      pdSentiment.innerHTML = "<h2>" + data.predicted_sentiment.toString() + "</h2>";
      console.log(status);
  });
}



