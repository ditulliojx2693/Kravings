function submit() {
  let http = new XMLHttpRequest();
  let url = '/quiz';
  http.open('POST', url, true);
  http.send();
  //Send the proper header information along with the request
}
function ifChecked () {
  let input1 = document.getElementsByName('burger1');
  let input2 = document.getElementsByName('ice_cream1');
  let input3 = document.getElementsByName('tofu1');
  let input4 = document.getElementsByName('beef1');
  let input5 = document.getElementsByName('seafood1');
  let quiz = document.getElementsByClassName('quiz');
  let falseCount1 = 0;
  for (a = 0; a < input1.length; a++){
    let check1 = input1[a].checked;
    if (check1){
      break
    }
    else{
      falseCount1 += 1;
    }
    if (falseCount1 == input1.length){
      alert("You forgot a box!");
    };
  let falseCount2 = 0;
  for (b = 0; b < input2.length; b++){
    let check2 = input2[b].checked;
    if (check2){
      break
    }
    else{
      falseCount2 += 1;
    }
    if (falseCount2 == input2.length){
      alert("You forgot a box!");
    };
  }
<<<<<<< HEAD
  else{
    submit();
=======
  };
  }
>>>>>>> ef4a93d68a3dcce699b5da2a99d134ff24493e82
