const express = require("express");
const app = express();
const PORT = 8080;

app.use(express.json()); //Middleware

app.listen(
    PORT,
    () => console.log(`Rest api running on port:${PORT}`)
)

app.get('/tshirt' , (req, res) => {
    console.log("GET ACTIVATED")
    return res.status(200).send({
        tshirt: 'T-Shirt',
        size: 'large'
    })
});

app.post('/movement', (req, res) => {
    console.log("Movement signal received")
    return res.send({
            response: 1, 
    })

    
})