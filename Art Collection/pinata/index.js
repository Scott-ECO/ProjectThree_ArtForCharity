const pinataSDK = require('@pinata/sdk');
require('dotenv').config()
const pinata = pinataSDK(process.env.PINATA_API_KEY, process.env.PINATA_SECRET_API_KEY);

pinata.testAuthentication().then((result) => {
    //handle successful authentication here
    console.log(result);
}).catch((err) => {
    //handle error here
    console.log(err);
});

const fs = require('fs');
const readableStreamForFile = fs.createReadStream('./images/butterfly.jpg');
const options = {
    pinataMetadata: {
        name: "Endangered NFT Collection",
        keyvalues: {
            customKey: 'customValue',
            customKey2: 'customValue2'
        }
    },
    pinataOptions: {
        cidVersion: 0
    }
};

const pinFileToIPFS = () => {
    return pinata.pinFileToIPFS(readableStreamForFile, options).then((result) => {

        return ('https://gateway.pinata.cloud/ipfs/' + result.IpfsHash)

    }).catch((err) => {
        //handle error here
        console.log(err);
    }); 
}

const pinJSONtoIPFS = (body) => {
    return pinata.pinJSONToIPFS(body, options).then((result) => {
        return ('https://gateway.pinata.cloud/ipfs/' + result.IpfsHash)
        console.log(result);
    }).catch((err) => {
        //handle error here
        console.log(err);
    });
}

const getMetadata = async () => {
    const imageUrl = await pinFileToIPFS()
    console.log(imageUrl)
    const body = {
        name: 'Monarch Butterfly',
        description: "This is a part of the Endangered NFT collection",
        image: imageUrl,
        attributes: [
            { "trait_type": "2022 Population", "value": "250,000-275,000" },      
            { "trait_type": "Status", "value": "Endangered" },      
            { "trait_type": "Habitat","value": "Grassland" },
        ]

    };

    const metadata = await pinJSONtoIPFS(body)
    console.log(metadata)

}

getMetadata()

// NFTs ranked by most endangered
// NFT 1 (Javan Rhino) = https://gateway.pinata.cloud/ipfs/QmPvrQkfUmD4VXtjVkmgaRBBogePret8hnUtFiiAp4mN9T
// NFT 2 (Mountain Gorilla) = https://gateway.pinata.cloud/ipfs/QmbirPd68hSQKUfaady28o8U4JaK3hqgS7zqdQ25LkRusx
// NFT 3 (Tiger) = https://gateway.pinata.cloud/ipfs/QmcYHED2XXC5jCTkRm87gb3jqaEHCW2xVgRE3WQAwW8rVT
// NFT 4 (Polar Bear) = https://gateway.pinata.cloud/ipfs/QmPKuUsBXTAikvex2AsfuS8uyxn3Z4PiX3rHfJh2vxm5MM
// NFT 5 (Plains Bison) = https://gateway.pinata.cloud/ipfs/QmX3nbnDLmvNzPzF19Gdauey5L3L4BTaUmNMEmbV2xF5Uv
// NFT 6 (African Forest Elephant) = https://gateway.pinata.cloud/ipfs/QmQuYBHsPZWGwz1E5oJKmEc3rgBy3BThkh8Y49USTfagau
// NFT 7 (Butterfly) = https://gateway.pinata.cloud/ipfs/QmcqcU8wm8mScwBqpMv4fUUbCkao3G1DyeYbEXzoPHhWiz
// NFT 8 (Sea Turtle) = https://gateway.pinata.cloud/ipfs/QmbpJHwXCBsaQ8tGvVNVu7jfKjp2VSS7axnKeFNCRAFvZb
