let frameNumber = 0;
let path = window.location.pathname;

frameNumber = parseInt(path.substring(path.lastIndexOf('/') + 1).match(/\d+/)[0]);

function changeWeb (nF){

    if(frameNumber === 3){
        sessionStorage.clear;
    } else {
        sessionStorage.clear;
        // Guardar un valor en sessionStorage
        sessionStorage.setItem('frame', frameNumber);
        sessionStorage.setItem('data', `Prueba ${frameNumber}`);
    }
     
    window.parent.postMessage(`web${nF}.html`, "*");
}

window.addEventListener('load', (event) =>{
    let result = document.getElementById('result');
    let fromFrame = sessionStorage.getItem('frame');
    let data = sessionStorage.getItem('data');
    if (data){
        let text = `<p>Data from frame ${fromFrame}</p>
                    <p>Data: ${data}</p>
                   `;
        if (result) result.innerHTML = text;
    }
    
});


