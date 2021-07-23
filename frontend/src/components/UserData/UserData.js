import React, { useState, useEffect } from "react";
import { getUserData } from "../../calls/getUserData";
import { isMobileCheck } from "../../helpers/checkMobileTablet";
import { Table } from "antd";

import "./UserData.css";

export const UserData = () => {
  const [userData, setUserData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const isMobile = isMobileCheck();

  const fetchUserData = async () => {
    try {
      const fetchedData = await getUserData();
      const fetchedDataWoEmoji = fetchedData.map((userData, index) => {
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
      });
      const fetchedDataWoEmojiFiltered = fetchedDataWoEmoji.filter((user) => {
        return user.first_name !== 'Group' && user.first_name !== 'Telegram'
      });
      setUserData(fetchedDataWoEmojiFiltered);
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
      title: "Telegram Id",
      dataIndex: "telegram_id",
      key: "telegram_id",
      sorter: (a, b) => a.telegram_id - b.telegram_id,
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
    {
      title: "First Name",
      dataIndex: "first_name",
      key: "first_name",
      defaultSortOrder: "descend",
      sorter: (a, b) => {
        if (!a.first_name) {
          return +1;
        }
        if (!b.first_name) {
          return -1;
        }
        return a.first_name.localeCompare(b.first_name);
      },
    },
    {
      title: "Last Name",
      dataIndex: "last_name",
      key: "last_name",
      defaultSortOrder: "descend",
      sorter: (a, b) => {
        if (!a.last_name) {
          return +1;
        }
        if (!b.last_name) {
          return -1;
        }
        return a.last_name.localeCompare(b.last_name);
      },
      responsive: ["lg"],
    },
    {
      title: "Activity",
      dataIndex: "activity",
      key: "activity",
      defaultSortOrder: "descend",
      sorter: (a, b) => a.activity - b.activity,
      responsive: ["lg"],
    },
    {
      title: "Join date",
      dataIndex: "joined_date",
      key: "joined_date",
      sorter: (a, b) => {
        if (!a.joined_date) {
          return +1;
        }
        if (!b.joined_date) {
          return -1;
        }
        return a.joined_date.localeCompare(b.joined_date);
      },
    },
    {
      title: "Last activity",
      dataIndex: "last_seen_date",
      key: "last_seen_date",
      sorter: (a, b) => {
        if (!a.last_seen_date) {
          return +1;
        }
        if (!b.last_seen_date) {
          return -1;
        }
        return a.last_seen_date.localeCompare(b.last_seen_date);
      },
    },
    {
      title: "Last meetup",
      dataIndex: "last_meetup",
      key: "last_meetup",
      sorter: (a, b) => {
        if (!a.last_meetup) {
          return +1;
        }
        if (!b.last_meetup) {
          return -1;
        }
        return a.last_meetup.localeCompare(b.last_meetup);
      },
    },
  ];

  useEffect(() => {
    fetchUserData();
  }, []);

  return isLoading ? (
    <div>Loading</div>
  ) : (
    <div className="ListUserData">
      <Table
        dataSource={userData}
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
