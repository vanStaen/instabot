import React, { useState, useEffect } from "react";
import {
  getAccountData,
  getAccountDataUserCount,
} from "../../calls/getAccountData";
import { postAccountAlive } from "../../calls/postAccountAlive";
import { postAccountActive } from "../../calls/postAccountActive";
import { isMobileCheck } from "../../helpers/checkMobileTablet";
import { Table, Switch } from "antd";

import "./AccountData.css";

export const AccountData = () => {
  const [accountData, setAccountData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const isMobile = isMobileCheck();

  const fetchAccountData = async () => {
    try {
      const fetchedData = await getAccountData();
      const fetchedDataWithCount = await fetchedData.map( async (accountData, index) => {
        const dataWithCount = {
          ...accountData,         
          count: await getAccountDataUserCount(accountData.username),
        };
        return dataWithCount;
      });
      console.log(fetchedDataWithCount);
      setAccountData(fetchedData);
    } catch (err) {
      console.log(err);
    }
    setIsLoading(false);
  };

  const switchHandlerAlive = async (id, value) => {
    const index = accountData.findIndex((accountData) => accountData.id == id);
    const accountDataTemp = accountData;
    accountDataTemp[index]["alive"] = !value;
    await postAccountAlive(accountDataTemp[index]["username"], !value);
    setAccountData(accountDataTemp);
  };

  const switchHandlerActive = async (id, value) => {
    const index = accountData.findIndex((accountData) => accountData.id == id);
    const accountDataTemp = accountData;
    accountDataTemp[index]["active"] = !value;
    await postAccountActive(accountDataTemp[index]["username"], !value);
    setAccountData(accountDataTemp);
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
    {
      title: "Iterations",
      dataIndex: "iterations",
      key: "iterations",
      sorter: (a, b) => a.id - b.id,
    },
    {
      title: "Count",
      dataIndex: "count",
      key: "count",
    },
    {
      title: "Tags",
      dataIndex: "tags",
      key: "tags",
    },
    {
      title: "Active",
      dataIndex: "active",
      key: "active",
      sorter: (a, b) => a.id - b.id,
      render: (text, record) => (
        <Switch
          defaultChecked={record.active}
          onClick={() => switchHandlerActive(record.id, record.active)}
        />
      ),
    },
    {
      title: "Alive",
      dataIndex: "alive",
      key: "alive",
      sorter: (a, b) => a.id - b.id,
      render: (text, record) => (
        <Switch
          defaultChecked={record.alive}
          onClick={() => switchHandlerAlive(record.id, record.alive)}
        />
      ),
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
        rowKey="id"
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
