import React, { useState, useEffect } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import ProductService from "../service/ProductService";

const Leaderboard = () => {
  const [products, setProducts] = useState([]);
  const productService = new ProductService();

  useEffect(() => {
    productService.getProductsSmall().then((data) => setProducts(data));
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <div>
      <div className="card">
        <DataTable value={products}>
          <Column field="name" header="Name"></Column>
          <Column field="score" header="Score"></Column>
          <Column field="date" header="Date"></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default Leaderboard;
