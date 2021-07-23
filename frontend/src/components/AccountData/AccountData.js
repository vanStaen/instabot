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
      const fetchedDataCleaned = fetchedData.map((accountData, index) => {
        const accountDataCleaned = {
          ...accountData,
          alive: accountData.alive ? 1 : 0,
          active: accountData.active ? 1 : 0,
        };
        return accountDataCleaned;
      });
      setAccountData(fetchedDataCleaned);
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
    {
      title: "Iterations",
      dataIndex: "iterations",
      key: "iterations",
      sorter: (a, b) => a.id - b.id,
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
    },
    {
      title: "Alive",
      dataIndex: "alive",
      key: "alive",
      sorter: (a, b) => a.id - b.id,
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
