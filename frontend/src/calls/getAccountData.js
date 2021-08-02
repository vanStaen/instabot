import axios from "axios";

export const getAccountData = async () => {
  const response = await axios({
    url: process.env.REACT_APP_API_URL + `/accounts`,
    method: "GET",
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

export const getAccountDataUserCount = async (account) => {
  const response = await axios({
    url: process.env.REACT_APP_API_URL + `/accounts/count/` + account.replace(".", ""),
    method: "GET",
  });

  if ((response.status !== 200) & (response.status !== 201)) {
    if (response.status === 401) {
      throw new Error(`Error! Unauthorized(401)`);
    } else {
      throw new Error(`Error! Status ${response.status}`);
    }
  }

  return response.data[0].count;
};
