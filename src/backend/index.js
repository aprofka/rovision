const express = require("express");
const app = express();
const PORT = 8080;

app.use(express.json()); //Middleware

app.listen(
    PORT,
    () => console.log(`Its alive on port:${PORT}`)
)

app.get('/tshirt' , (req, res) => {
    res.status(200).send({
        tshirt: 'T-Shirt',
        size: 'large'
    })
});

app.post('/tshirt/:id', (req, res) => {
    const { id } = req.params;
    const { logo } = req.body;

    if (!logo) {
        res.status(418).send({messeage: 'A logo is needed!'})
    }

    res.send({
            tshirt: `tshirt with your ${logo} and ID of ${id}`, 
    })
})