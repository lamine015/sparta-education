# DataBricks & PySpark

## Big data

Big Data refers to extremely large and fast-growing datasets that are too complex for traditional data processing tools to store, manage, or analyse efficiently. Traditional tools include relational databases like Microsoft Access or older MySQL/PostgreSQL setups, as well as spreadsheet software such as Microsoft Excel, which struggle with very large or continuously streaming datasets. It includes data from many different sources and formats, such as structured data like database tables, semi-structured data like JSON or XML files, and unstructured data like emails, documents, images, audio, and video.

## OLTP vs OLAP

OLTP (Online Transaction Processing) and OLAP (Online Analytical Processing) are both ways of working with data, but they are designed for very different purposes.

### OLTP (Online Transaction Processing)
OLTP systems are used for day-to-day operations where data is constantly being added, updated, or deleted. They focus on speed and accuracy for individual transactions, such as placing an order, making a payment, or booking a ticket. These systems are used in real-time applications and are designed to handle many users at once.

OLTP systems also follow something called **ACID properties**, which ensure transactions are processed safely and correctly:
- **Atomicity:** A transaction is all or nothing (it fully completes or doesn’t happen at all)
- **Consistency:** Data remains accurate and follows all rules before and after a transaction
- **Isolation:** Multiple transactions can happen at the same time without interfering with each other
- **Durability:** Once a transaction is completed, it is permanently saved even if the system crashes

### OLAP (Online Analytical Processing)
OLAP systems, on the other hand, are used for analysing large amounts of historical data. Instead of focusing on single transactions, OLAP looks at trends, patterns, and summaries to help with decision-making. For example, a business might use OLAP to analyse yearly sales performance or customer behaviour.

## Key Differences

- **Purpose:**  
  OLTP handles daily operations, OLAP handles analysis and reporting  

- **Data Type:**  
  OLTP uses current, detailed data; OLAP uses historical, aggregated data  

- **Operations:**  
  OLTP focuses on insert/update/delete; OLAP focuses on complex queries and read operations  

- **Speed:**  
  OLTP is optimised for fast transactions; OLAP is optimised for fast data analysis  

- **Examples:**  
  OLTP → online banking, e-commerce checkout  
  OLAP → dashboards, business intelligence reports  

## Data Storage and Processing Systems

After understanding OLTP and OLAP, it’s important to look at the main systems used to store and process data at scale.

## Data Warehouses

A **data warehouse** is a central system used to store large amounts of structured and historical data from multiple sources. It is designed for reporting, dashboards, and business analysis.

### How Data Warehouses Work
Data is taken from different operational systems (like OLTP databases), cleaned, and transformed before being loaded into the warehouse. This process is known as **ETL (Extract, Transform, Load)**. The data is then organised so it can be queried efficiently for analytics.

---

## Data Lakes

A **data lake** is a storage system that holds large volumes of raw data in its original format, including structured, semi-structured, and unstructured data.

### How Data Lakes Work
Data is stored first without strict structure, and processing happens later when needed. This makes data lakes flexible and suitable for data science, machine learning, and big data workloads. However, without proper management, they can become disorganised (“data swamps”).

---

## Data Lakehouses

A **data lakehouse** combines the strengths of data lakes and data warehouses into one system.

### How Data Lakehouses Work
Data is stored in a low-cost data lake, but with added structure, metadata, and performance optimisations that allow fast SQL analytics. This means you get the flexibility of a lake and the organisation of a warehouse in one platform.

---

## Delta Lakes

A **Delta Lake** is a storage layer built on top of a data lake that improves reliability and performance. It is commonly used in Databricks environments.

### How Delta Lakes Work
Delta Lakes add features such as **ACID transactions**, schema enforcement, and data versioning (time travel). This ensures that data updates are reliable, consistent, and trackable over time, even in large-scale data pipelines.

---

## Summary

- **OLTP:** Real-time transactional systems  
- **OLAP:** Analytical systems for insights and reporting  
- **Data Warehouse:** Structured, cleaned data for analytics  
- **Data Lake:** Raw, flexible storage for all data types  
- **Data Lakehouse:** Combines lake flexibility with warehouse structure  
- **Delta Lake:** Adds reliability (ACID + version control) to data lakes 

---

# Apache Spark and PySpark

As the volume of data grew, traditional data processing tools became too slow and expensive for large-scale analytics. Apache Spark was developed to process big data quickly across multiple machines.

## What is Apache Spark?

Apache Spark is an open-source distributed data processing framework designed for large-scale data analytics. It allows data to be processed across clusters of computers, making it much faster than traditional single-machine processing.

Spark supports a wide range of workloads including:
- Batch processing
- Real-time stream processing
- Machine learning
- Graph processing
- SQL analytics

---

## What Problem Did Apache Spark Solve?

Before Spark, many organisations used Hadoop MapReduce for big data processing. While powerful, MapReduce had some limitations:

- Data was repeatedly written to and read from disk
- Processing jobs could be slow
- Complex workflows required multiple MapReduce jobs
- Development was often complicated

Spark solved these problems by processing data primarily **in memory**, significantly reducing disk I/O and improving performance. This made data processing much faster and more efficient.

---

## How Does Apache Spark Work?

Spark distributes data and processing tasks across multiple machines in a cluster.

When a Spark job is submitted:

1. The **Driver Program** creates and coordinates the job.
2. The Driver divides the work into smaller tasks.
3. Tasks are distributed to **Worker Nodes**.
4. Workers process their assigned data in parallel.
5. Results are returned to the Driver.

Because many machines work on the data simultaneously, Spark can process massive datasets much faster than a single computer.

### Spark Architecture

The main components of Spark are:

- **Driver** – Controls and coordinates the Spark application.
- **Cluster Manager** – Allocates resources across the cluster.
- **Worker Nodes** – Machines that perform the processing.
- **Executors** – Processes running on worker nodes that execute tasks and store data in memory.

A simplified flow looks like this:

```text
Driver Program
       |
       v
Cluster Manager
       |
       v
--------------------------------
| Worker | Worker | Worker |
| Node   | Node   | Node   |
--------------------------------
     |        |        |
 Executors Executors Executors
```
---

# Databricks

## What is Databricks?

Databricks is a cloud-based data platform built on top of Apache Spark. It provides a unified environment where data engineers, data analysts, data scientists, and machine learning engineers can collaborate using the same tools and data.

---

## What Problems Did Databricks Solve?

Although Apache Spark is a powerful processing engine, managing clusters, infrastructure, and workflows can be complex. Databricks simplifies this by automating cluster management, providing collaborative workspaces, and integrating data engineering, analytics, and machine learning into a single platform.

---

## How Does Databricks Work?

Databricks allows users to write code in notebooks using languages such as Python, SQL, Scala, and R. Behind the scenes, it automatically manages Spark clusters and computing resources, allowing users to focus on processing and analysing data rather than configuring infrastructure.

---

## Why Has Databricks Become Popular?

Databricks has become popular because it makes big data processing easier and more accessible. It reduces the complexity of working with Apache Spark while providing tools for collaboration, automation, and scalable data processing.

---

## Key Features of Databricks

- **Collaborative Notebooks** – Multiple users can work on the same notebooks.
- **Managed Spark Clusters** – Automatic cluster creation and scaling.
- **Delta Lake Integration** – Reliable data storage with ACID transactions.
- **Workflow Automation** – Schedule and manage data pipelines.
- **Multi-Language Support** – Supports Python, SQL, Scala, and R.
- **Machine Learning Tools** – Build and deploy machine learning models.
- **Cloud Integration** – Works with AWS, Azure, and Google Cloud.

---

## Summary

Databricks is a platform built on Apache Spark that simplifies big data processing, collaboration, and analytics. It allows organisations to process large datasets efficiently without needing to manage the underlying infrastructure themselves.