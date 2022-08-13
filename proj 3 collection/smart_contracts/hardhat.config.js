require("@nomiclabs/hardhat-waffle")
require("@nomiclabs/hardhat-etherscan")
require("dotenv").config()

module.exports = {
  solidity: "0.8.4",
  networks: {
    rinkedby: {
      url: process.env.RINKEDBY_API,
      accounts: [process.env.PRIVATE_KEY]
    }
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API
  }
};
