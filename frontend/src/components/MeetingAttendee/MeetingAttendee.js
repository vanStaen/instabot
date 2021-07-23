import React, { useState, useEffect } from "react";
import { getUserData } from "../../calls/getUserData";
import { postAttendee } from "../../calls/postAttendee";
import { isMobileCheck } from "../../helpers/checkMobileTablet";
import { Table, Switch } from "antd";

import "./MeetingAttendee.css";

export const MeetingAttendee = () => {
  const [userData, setUserData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const switchHandler = (id) => {
    const index = userData.findIndex(userData => userData.id == id)
    const userDataTemp = userData;
    userDataTemp[index]['last_meetup']='2021-07-09';
    postAttendee(id);
    setUserData(userDataTemp);
  }

  const isMobile = isMobileCheck();

  const fetchUserData = async () => {
    try {
      const fetchedData = await getUserData();
      const fetchedDataWoEmoji = fetchedData.map((userData, index) => {
        const userDataWoEmoji = {
          ...userData,
          key: `key_${index}`,
          username: userData.username && userData.username.replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, ''),
          first_name:  userData.first_name && userData.first_name.replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, ''),
          last_name:  userData.last_name && userData.last_name.replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, ''),
          last_meetup:  userData.last_meetup && 'Present',
        }
        return userDataWoEmoji
      });
      setUserData(fetchedDataWoEmoji);
    } catch (err) {
      console.log(err);
    }
    setIsLoading(false);
  };

  const columns = [
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
      responsive: ['lg'],
    },
    {
      title: 'Check',
      key: 'action',
      width: isMobile ? 50 : 100,
      render: (text, record) => (
        <Switch defaultChecked={record.last_meetup} onClick={() => switchHandler(record.id, record.last_meetup)}/>
      ),
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
    <div className="MeetingAttendee">
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
