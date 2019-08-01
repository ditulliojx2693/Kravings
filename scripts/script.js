function ifChecked () {
  let input1 = document.getElementsByName('burger1');
  let input2 = document.getElementsByName('ice_cream1');
  let input3 = document.getElementsByName('tofu1');
  let input4 = document.getElementsByName('beef1');
  let input5 = document.getElementsByName('seafood1');
  let input6 = document.getElementsByName('burger2');
  let input7 = document.getElementsByName('ice_cream2');
  let input8 = document.getElementsByName('tofu2');
  let input9 = document.getElementsByName('beef2');
  let input10 = document.getElementsByName('seafood2');
  let quiz = document.getElementsByClassName('quiz');
  let falseCount1 = 0;
  for (a = 0; a < input1.length; a++){
    let check1 = input1[a].checked;
    if (check1){
      break
    }
    else{
      falseCount1 += 1;
    }};
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
    }};
    let falseCount3 = 0;
    for (c = 0; c < input3.length; c++){
      let check3 = input3[c].checked;
      if (check3){
        break
      }
      else{
        falseCount3 += 1;
      }};
  let falseCount4 = 0;
  for (d = 0; d < input4.length; d++){
    let check4 = input4[d].checked;
    if (check4){
      break
    }
    else{
      falseCount4 += 1;
    } };
  let falseCount5 = 0;
  for (e = 0; e < input5.length; e++){
    let check5 = input5[e].checked;
    if (check5){
      break
    }
    else{
      falseCount5 += 1;
    }
  };
  let falseCount6 = 0;
  for (f = 0; f < input6.length; f++){
    let check6 = input6[f].checked;
    if (check6){
      break
    }
    else{
      falseCount6 += 1;
    }
  };
  let falseCount7 = 0;
  for (g = 0; g < input7.length; g++){
    let check7 = input7[g].checked;
    if (check7){
      break
    }
    else{
      falseCount7 += 1;
    }
  };
  let falseCount8 = 0;
  for (h = 0; h < input8.length; h++){
    let check8 = input8[h].checked;
    if (check8){
      break
    }
    else{
      falseCount8 += 1;
    }
  };
  let falseCount9 = 0;
  for (i = 0; i < input9.length; i++){
    let check9 = input9[i].checked;
    if (check9){
      break
    }
    else{
      falseCount9 += 1;
    }
  };
  let falseCount10 = 0;
  for (j = 0; j < input5.length; j++){
    let check10 = input10[j].checked;
    if (check10){
      break
    }
    else{
      falseCount10 += 1;
    }
  };
  if (falseCount1 == input1.length || falseCount2 == input2.length || falseCount3 == input3.length || falseCount4 == input4.length || falseCount5 == input5.length || falseCount6 == input6.length || falseCount7 == input7.length || falseCount8 == input8.length || falseCount9 == input9.length || falseCount10 == input10.length){
    alert("You forgot a box!");
    if (falseCount2 == input2.length){
      alert("You forgot a box!");
    };
  }
  else{
    quiz[0].submit();
  };
 }

function check() {
  let password = document.getElementById('password')
  let username = document.getElementById('username')
  let logIn = document.getElementById('logIn')
  if (password.value == "" && username.value == ""){
    alert("Fill all boxes!")
  }
  else if (password.value == ""){
    alert('Fill in the password box!');
  }
  else if(username.value == ""){
    alert('Fill in the username box!');
  }
  else{
    logIn.submit();
  }
}
function signUpCheck(){
  let password = document.getElementById('password1')
  let username = document.getElementById('username1')
  let firstName = document.getElementById('firstName')
  let lastName = document.getElementById('lastName')
  let signUp = document.getElementById('signUp')
  if (firstName.value == ""){
    alert("Fill in your first name")
  }
  else if(lastName.value == ""){
    alert("Fill in your last name")
  }
  else if(username.value == ""){
    alert("Fill in your username")
  }
  else if(password.value == ""){
    alert("Fill in your password")
  }
  else{
    signUp.submit()
  }
}

function randomizeFood(){
  randomNumber = Math.floor(Math.random() * 10) + 1;
  alert("Working")
  if (randomNumber == 1){
    randImg = "images/burger.png"
    randFoodItem = "A Burger"
  }
}
