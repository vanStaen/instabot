import axios from "axios";

export const postAttendee = async (id) => {

    const requestBody = {
        "last_meetup": '2021-07-09',
        "id": id,
    };

    const response = await axios({
        url: process.env.REACT_APP_API_URL + `/users/meetup`,
        method: "POST",
        data: requestBody,
        
    });

    if ((response.status !== 200) & (response.status !== 201)) {
        if (response.status === 401) {
            throw new Error(`Error! Unauthorized(401)`);
        } else {
            throw new Error(`Error! Status ${response.status}`);
        }
    }

    return response.data;
};