function previewImage(){

    const file = document.getElementById("image").files[0];
    const reader = new FileReader();

    reader.onload = function(e){
        document.getElementById("preview").src = e.target.result;
    }

    if(file){
    reader.readAsDataURL(file);
    }
}


async function uploadOCR(){

    const file = document.getElementById("image").files[0];
    const api = document.getElementById("ocr_type").value;

    if(!file){
        alert("Upload image first");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    document.getElementById("loader").style.display = "block";

    try{

        const response = await fetch("http://127.0.0.1:8000/" + api,{
            method:"POST",
            body:formData
        });

        const data = await response.json();

        console.log("OCR RESPONSE:", data);

        document.getElementById("doc_number").value =
            data.pan_number ||
            data.aadhar_number ||
            data.passport_number ||
            "";

        document.getElementById("name").value =
            data.name ||
            "";

        document.getElementById("father_name").value =
            data.father_name || "";

        document.getElementById("dob").value =
            data.dob ||
            data.date_of_birth ||
            "";

        document.getElementById("gender").value =
            data.gender || "";

        document.getElementById("nationality").value =
            data.nationality || "";

        document.getElementById("expiry").value =
            data.expiry ||
            data.expiry_date ||
            "";

        document.getElementById("raw_text").value =
            data.raw_text ||
            data.extracted_text ||
            "";

        /* CONFIDENCE BAR */
        if(data.confidence_score){
            let percent = Math.round(data.confidence_score * 100);
            let bar = document.getElementById("confidence_bar");
            bar.style.width = percent + "%";
            bar.innerText = percent + "%";
        }

    }catch(error){
        alert("OCR failed");
        console.error(error);
    }

    document.getElementById("loader").style.display = "none";
}