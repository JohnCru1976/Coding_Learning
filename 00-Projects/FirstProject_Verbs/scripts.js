// Creation of a class to manage the verbs testing
function Verbs(verbs, numTestP){    
    let testedVerbsId = [];
    let totalVerbs = verbs.length;
    let actualVerb;
    let actualPosition;
    let inputVerbs = [];
    let originalVerbs = [];
    this.getTraslation = function(){
        return actualVerb["translation"];
    };
    this.restart = function(){
        testedVerbsId = [];
        inputVerbs = [];
        originalVerbs = [];
    };
    this.position = function(){
       return "Verb " + testedVerbsId.length + "/" + numTestP;
    };
    this.checkComplete = function(){
       return testedVerbsId.length >= numTestP;
    };
    this.newVerb = function(){
        actualPosition = Math.floor(Math.random()*totalVerbs); 
        while(testedVerbsId.some((elem) => elem == actualPosition) && testedVerbsId.length < numTestP){
            actualPosition = Math.floor(Math.random()*totalVerbs);
        }
        if(testedVerbsId.length < numTestP){
            actualVerb = verbs[actualPosition];
            testedVerbsId.push(actualPosition);
            return actualVerb;
        }
        return undefined;
    };
    this.assessVerb = function(infinitive, past, participle){
        let newInput = {};
        newInput.infinitive = infinitive.toLowerCase();
        newInput.past = past.toLowerCase();
        newInput.participle = participle.toLowerCase();
        inputVerbs.push(newInput);
        originalVerbs.push(actualVerb);
    };
    this.getActualVerb = function(){
        return actualVerb;
    };
    this.getActualposition = function(){
        return actualPosition;
    };
    this.getInputVerbs = function(){
        return inputVerbs;
    };
    this.getOriginalVerbs = function(){
        return originalVerbs;
    };
     this.getTestedVerbsId = function(){
        return testedVerbsId;
    };
}

const verbsArray = [
    {infinitive:"be", past:"was/were", participle:"been", translation:"ser/estar"},
    {infinitive:"become", past:"became", participle:"become", translation:"convertirse"},
    {infinitive:"begin", past:"began", participle:"begun", translation:"empezar"},
    {infinitive:"break", past:"broke", participle:"broken", translation:"romper"},
    {infinitive:"bring", past:"brought", participle:"brought", translation:"traer"},
    {infinitive:"build", past:"built", participle:"built", translation:"construir"},
    {infinitive:"buy", past:"bought", participle:"bought", translation:"comprar"},
    {infinitive:"catch", past:"caught", participle:"caught", translation:"coger"},
    {infinitive:"choose", past:"chose", participle:"chosen", translation:"elegir"},
    {infinitive:"come", past:"came", participle:"come", translation:"venir"},
    {infinitive:"cost", past:"cost", participle:"cost", translation:"costar"},
    {infinitive:"do", past:"did", participle:"done", translation:"hacer"},
    {infinitive:"dream", past:"dreamed", participle:"dreamed", translation:"soñar"},
    {infinitive:"drive", past:"drove", participle:"driven", translation:"conducir"},
    {infinitive:"drink", past:"drank", participle:"drunk", translation:"beber"},
    {infinitive:"eat", past:"ate", participle:"eaten", translation:"comer"},
    {infinitive:"fall", past:"fell", participle:"fallen", translation:"caer"},
    {infinitive:"find", past:"found", participle:"found", translation:"encontrar"},
    {infinitive:"feel", past:"felt", participle:"felt", translation:"sentir"},
    {infinitive:"fly", past:"flew", participle:"flown", translation:"volar"},
    {infinitive:"forget", past:"forgot", participle:"forgotten", translation:"olvidar"},
    {infinitive:"get", past:"got", participle:"got", translation:"conseguir/obtener"},
    {infinitive:"give", past:"gave", participle:"given", translation:"dar"},
    {infinitive:"go", past:"went", participle:"gone", translation:"ir"},
    {infinitive:"have", past:"had", participle:"had", translation:"tener/haber"},
    {infinitive:"hear", past:"heard", participle:"heard", translation:"escuchar"},
    {infinitive:"know", past:"knew", participle:"known", translation:"conocer"},
    {infinitive:"learn", past:"learned", participle:"learned", translation:"aprender"},
    {infinitive:"leave", past:"left", participle:"left", translation:"salir/dejar"},
    {infinitive:"lose", past:"lost", participle:"lost", translation:"perder"},
    {infinitive:"make", past:"made", participle:"made", translation:"hacer/elaborar"},
    {infinitive:"pay", past:"paid", participle:"paid", translation:"pagar"}
]

let verbManaging;

window.onload = function (){
    document.getElementById("num_verbs").max = verbsArray.length;
    
    document.getElementById("infinitive").addEventListener('keydown', keypress);
    document.getElementById("past").addEventListener('keydown', keypress);
    document.getElementById("participle").addEventListener('keydown', keypress);
    
    showSection(1);
}

const keypress = ({key})=>{
    let keyAscii = key.charCodeAt(0);
    
    if ((keyAscii === 69 || keyAscii === 32) && document.getElementById("infinitive").value.trim() != "" & 
            document.getElementById("past").value.trim() != "" &
            document.getElementById("participle").value.trim() != "") {
        clickNextButton();
    } else if(keyAscii === 69 || keyAscii === 32){
        if(document.getElementById("infinitive").value.trim() === ""){
            document.getElementById("infinitive").focus();
            return false;
        } else if(document.getElementById("past").value.trim() === ""){
            document.getElementById("past").focus();
            return false;
        } else if(document.getElementById("participle").value.trim() === ""){
            document.getElementById("participle").focus();
            return false;
        }
    }
};

function showSection (n){
    // Shows only the section pass as n parameter
    let section1 = document.getElementById("start_section");
    let section2 = document.getElementById("verbs_section");
    let section3 = document.getElementById("final_result");
    section1.hidden = true;
    section2.hidden = true;
    section3.hidden = true;
    if(n==1){
        section1.hidden = false;
    }
    if(n==2){
        verbManaging = new Verbs(verbsArray, document.getElementById("num_verbs").value);
        if(document.getElementById("num_verbs").value < 1 ||
           document.getElementById("num_verbs").value > verbsArray.length){
            document.getElementById("num_verbs").focus();
            showSection (1);
            alert("Introduce a valid number!!");
            return;
        }
        section2.hidden = false;
        clickNextButton();
    }
    if(n==3){
        section3.hidden = false;
        gettingResult();
    }
}

function clickNextButton(){
    if(verbManaging.getTestedVerbsId().length > 0){
        if(document.getElementById("infinitive").value.trim() === ""){
            document.getElementById("infinitive").focus();
            alert("Fill all the fields!!");
            return;
        } else if(document.getElementById("past").value.trim() === ""){
            document.getElementById("past").focus();
            alert("Fill all the fields!!");
            return;
        } else if(document.getElementById("participle").value.trim() === ""){
            document.getElementById("participle").focus();
            alert("Fill all the fields!!");
            return;
        }
    }
    document.getElementById("infinitive").disabled = false;
    document.getElementById("past").disabled = false;
    document.getElementById("participle").disabled = false;
    if(verbManaging.getTestedVerbsId().length > 0){
        let inf = document.getElementById("infinitive").value.trim();
        let pas = document.getElementById("past").value.trim();
        let par = document.getElementById("participle").value.trim();
        verbManaging.assessVerb(inf,pas,par);
        document.getElementById("infinitive").value = "";
        document.getElementById("past").value = "";
        document.getElementById("participle").value = "";
    }
    if(verbManaging.checkComplete()){
        showSection(3);
        return;
    }
    verbManaging.newVerb();
    document.getElementById("traslation").innerHTML = "Click here for translation";
    let verbPosition = document.getElementById("verb_number");
    verbPosition.innerHTML = verbManaging.position();
    let verb = verbManaging.getActualVerb();
    let randomTense = Math.floor(Math.random()*3);
    switch(randomTense){
        case 0:
            document.getElementById("infinitive").value = verb["infinitive"];
            document.getElementById("infinitive").disabled = true;
            document.getElementById("past").focus();
            break;
        case 1:
            document.getElementById("past").value  = verb["past"];
            document.getElementById("past").disabled = true;
            document.getElementById("infinitive").focus();
        
            break;
        case 2:
            document.getElementById("participle").value  = verb["participle"];
            document.getElementById("participle").disabled = true;
            document.getElementById("infinitive").focus();
            break;           
    }
}

function gettingResult(){
    let stringResult;
    let correctVerbsArray = verbManaging.getOriginalVerbs();
    let answeredVerbsArray = verbManaging.getInputVerbs();
    let count = 0;
    stringResult = "<ol>";    
    for(let i = 0; i < correctVerbsArray.length;i++){
        stringResult += "<li>Correct: " + firstLetterUpperCase(correctVerbsArray[i]["infinitive"]) + 
                        " - " + firstLetterUpperCase(correctVerbsArray[i]["past"]) + 
                        " - " + firstLetterUpperCase(correctVerbsArray[i]["participle"]) + "<br>" + 
                        "Answer: " + firstLetterUpperCase(answeredVerbsArray[i]["infinitive"]) + 
                        " - " + firstLetterUpperCase(answeredVerbsArray[i]["past"]) + 
                        " - " + firstLetterUpperCase(answeredVerbsArray[i]["participle"]);
                        
        if (correctVerbsArray[i]["infinitive"] == answeredVerbsArray[i]["infinitive"] &&
        correctVerbsArray[i]["past"] == answeredVerbsArray[i]["past"] &&
        correctVerbsArray[i]["participle"] == answeredVerbsArray[i]["participle"]){
            stringResult += "<br>(+1)</li>";
            count++;
        } else {
            stringResult += "<br>(+0)</li>";
        }
        
    }
    let tempResult = stringResult;
    stringResult = "<h2>" + count + " hits of " + correctVerbsArray.length;

    if((count*10)%correctVerbsArray.length === 0){
        stringResult += "<br>Score: " + ((count/correctVerbsArray.length)*10) + "/10</h2><br>";
    }else{
        stringResult += "<br>Score: " + ((count/correctVerbsArray.length)*10).toFixed(2) + "/10</h2><br>";
    }          
    stringResult += tempResult + "</ol>" ;

    document.getElementById("results").innerHTML = stringResult;
}

function clickRestart(){
    verbManaging.restart();
    document.getElementById("num_verbs").max = verbsArray.length;
    
    showSection(1);
}

function clickTraslation(){
        document.getElementById("traslation").innerHTML = firstLetterUpperCase(verbManaging.getTraslation());
        setTimeout(()=>{document.getElementById("traslation").innerHTML = "Click here for translation";},1000);
}

function firstLetterUpperCase (str){
    let firstLetter = str.charAt(0).toUpperCase();
    let restWord = str.slice(1);
    return firstLetter + restWord;
}