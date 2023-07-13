
 <title>Painting Classifier</title>

<input id="photo" type="file">
<div id="results"></div>
<script>
    async function loaded(reader) {   
    const response = await fetch("https://nifulislam-painting-classification.hf.space/run/predict", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({data: [reader.result]})});
    const json = await response.json();
    const label = json['data'][0]['label'];
    results.innerHTML = `<br/> <img src = "${reader.result}" width="500"> <p>${label}</p>`;
    }
    function read() {
        const reader = new FileReader();
        reader.addEventListener('load', () => loaded(reader))
        reader.readAsDataURL(photo.files[0]);
    }
    photo.addEventListener('input', read);
</script>


# Image Classifier
This image classifier can classify 10 tyepes of painging. The types are: <br>
1. Landscape
2. Portrait
3. Still Life
4. Abstract
5. Impressionist
6. Cubist
7. Surrealist
8. Expressionist
9. Realist
10. Pop Art
