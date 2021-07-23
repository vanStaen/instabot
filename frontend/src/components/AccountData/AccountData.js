import React, { useState, useEffect } from "react";
import { getAccountData } from "../../calls/getAccountData";
import { isMobileCheck } from "../../helpers/checkMobileTablet";
import { Table } from "antd";

import "./AccountData.css";

export const AccountData = () => {
  const [accountData, setAccountData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const isMobile = isMobileCheck();

  const fetchAccountData = async () => {
    try {
      const fetchedData = await getAccountData();
      /* const fetchedDataWoEmoji = fetchedData.map((userData, index) => {
        const userDataWoEmoji = {
          ...userData,
          key: `key_${index}`,
          username:
            userData.username &&
            userData.username.replace(
              /([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g,
              ""
            ),
          first_name:
            userData.first_name &&
            userData.first_name.replace(
              /([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g,
              ""
            ),
          last_name:
            userData.last_name &&
            userData.last_name.replace(
              /([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g,
              ""
            ),
        };
        return userDataWoEmoji;
      }); */
      /* const fetchedDataWoEmojiFiltered = fetchedDataWoEmoji.filter((user) => {
        return user.first_name !== 'Group' && user.first_name !== 'Telegram'
      }); */
      setAccountData(fetchedData);
    } catch (err) {
      console.log(err);
    }
    setIsLoading(false);
  };

  const columns = [
    {
      title: "id",
      dataIndex: "id",
      key: "id",
      sorter: (a, b) => a.id - b.id,
      responsive: ["lg"],
    },
    {
      title: "Username",
      dataIndex: "username",
      key: "username",
      defaultSortOrder: "ascend",
      sorter: (a, b) => {
        if (!a.username) {
          return +1;
        }
        if (!b.username) {
          return -1;
        }
        return a.username.localeCompare(b.username);
      },
    },
  ];

  useEffect(() => {
    fetchAccountData();
  }, []);

  return isLoading ? (
    <div>Loading</div>
  ) : (
      <div className="ListData">
        <Table
          dataSource={accountData}
          columns={columns}
          pagination={{
            position: ["bottomCenter"],
            defaultPageSize: "20",
            hideOnSinglePage: true,
          }}
          size={isMobile ? "small" : "large"}
        />
      </div>
    );
};
