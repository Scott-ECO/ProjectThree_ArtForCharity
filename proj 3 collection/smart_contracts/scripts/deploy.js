const hre = require("hardhat");


async function main() {
  const Endangered = await hre.ethers.getContractFactory("Endangered");
  const endangered = await Endangered.deploy();

  await endangered.deployed();

  console.log("Collection deployed to:", endangered.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });