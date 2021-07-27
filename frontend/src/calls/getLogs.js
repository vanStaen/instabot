import axios from "axios";

export const getLogs = async () => {

    const response = await axios({
        url: process.env.REACT_APP_API_URL + `/log`,
        method: "GET",
    });

    if ((response.status !== 200) & (response.status !== 201)) {
        if (response.status === 401) {
            throw new Error(`Error! Unauthorized(401)`);
        } else {
            throw new Error(`Error! Status ${response.status}`);
        }
    }

    const responseReformated = response.data.replaceAll("\"", "")
        .replaceAll("'", "\"")
        .replaceAll(/\\n/g, "\\n")  
        .replaceAll(/\\'/g, "\\'")
        .replaceAll(/\\"/g, '\\"')
        .replaceAll(/\\&/g, "\\&")
        .replaceAll(/\\r/g, "\\r")
        .replaceAll(/\\t/g, "\\t")
        .replaceAll(/\\b/g, "\\b")
        .replaceAll(/\\f/g, "\\f")
        .replaceAll(/[\u0000-\u0019]+/g,""); 
    const  responseReformated2 = responseReformated.substring(0, responseReformated.length - 1);
    const responseAsJson = JSON.parse(`[${responseReformated2}]`)
    
    return responseAsJson;
};