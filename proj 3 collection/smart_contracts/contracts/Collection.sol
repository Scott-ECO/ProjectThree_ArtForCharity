// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Endangered is ERC721URIStorage, Ownable {
    
    uint256 tokenId = 0;

    constructor() ERC721("Endangered", "END") {}

    function mint(string memory uri) public onlyOwner {
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);
        tokenId++;
    }
}