
function ifChecked () {
  let input1 = document.getElementsByName('burger1');
  let input2 = document.getElementsByName('ice_cream1');
  let input3 = document.getElementsByName('tofu1');
  let input4 = document.getElementsByName('beef1');
  let input5 = document.getElementsByName('seafood1');
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
    };}
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
    };}
    let falseCount3 = 0;
    for (c = 0; c < input3.length; c++){
      let check3 = input3[c].checked;
      if (check3){
        break
      }
      else{
        falseCount3 += 1;
      }
      if (falseCount3 == input3.length){
        alert("You forgot a box!");
      }}
  let falseCount4 = 0;
  for (d = 0; d < input4.length; d++){
    let check4 = input4[b].checked;
    if (check4){
      break
    }
    else{
      falseCount4 += 1;
    }
    if (falseCount4 == input4.length){
      alert("You forgot a box!");
    }; };
  let falseCount5 = 0;
  for (e = 0; e < input5.length; e++){
    let check5 = input5[e].checked;
    if (check5){
      break
    }
    else{
      falseCount5 += 1;
    }
    if (falseCount5 == input5.length){
      alert("You forgot a box!");
    };
  }; }
