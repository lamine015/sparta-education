# Introduction to MongoDB

## What is MongoDB?

**MongoDB** is a NoSQL database that stores data in JSON-like documents called **BSON** (Binary JSON). Unlike traditional relational databases, MongoDB does not store data in tables and rows. Instead, it stores data in **collections** and **documents**.

MongoDB is designed to handle large amounts of data while providing flexibility in how that data is structured. This makes it a popular choice for modern applications where requirements can change frequently.

## Relational Databases vs MongoDB

| Relational Database | MongoDB    |
| ------------------- | ---------- |
| Database            | Database   |
| Table               | Collection |
| Row                 | Document   |
| Column              | Field      |

## Example Document

```javascript
{
    name: "Mohamed Aboudaoud",
    age: 30,
    city: "London"
}
```

In this example:

* `name`, `age`, and `city` are fields.
* `"Mohamed Aboudaoud"`, `30`, and `"London"` are values.
* The entire record is known as a document.

## Why Use MongoDB?

MongoDB is commonly used because it allows developers to store data without requiring a fixed structure. This makes it easier to adapt applications as requirements change.

MongoDB is also designed to work well with large datasets and can scale across multiple servers when needed.

## Advantages of MongoDB

* Flexible schema design.
* Easy to store complex and nested data.
* Good performance for large datasets.
* Supports horizontal scaling.
* Works well with modern programming languages such as Python and JavaScript.
* Simple document structure that is easy to understand.

## Disadvantages of MongoDB

* Less structured than relational databases.
* Can lead to inconsistent data if not designed carefully.
* Complex relationships between data can be more difficult to manage.
* Not always the best choice for applications that require many joins and strict data integrity.

## Common Use Cases

MongoDB is commonly used for:

* E-commerce applications
* Content management systems (CMS)
* Social media platforms
* Real-time analytics
* Internet of Things (IoT) applications
* User profile and account management

## Relationships in MongoDB: Embedding vs Referencing

In MongoDB, data is often related to other data. Unlike relational databases, MongoDB does not use joins in the same way. Instead, relationships are handled in two main ways: **embedding** and **referencing**.

---

## 1. Embedding (Storing data inside a document)

Embedding means storing related data directly inside a document.

### Example

```javascript
{
    name: "Luke Skywalker",
    age: 25,
    address: {
        city: "Tatooine",
        planet: "Tatooine"
    }
}
```

In this example:

* The `address` field is an embedded document.
* All related data is stored together in one place.

### When to use embedding

* When data is closely related.
* When you often need to read the data together.
* When the embedded data does not change frequently.

### Advantages

* Faster reads (everything is in one document).
* Simple structure.
* No need to join data from different collections.

### Disadvantages

* Data duplication can happen.
* Harder to update if embedded data is used in many places.

---

## 2. Referencing (Linking documents together)

Referencing means storing relationships using an ID that points to another document.

### Example

**Character document:**

```javascript
{
    _id: ObjectId("123"),
    name: "Luke Skywalker"
}
```

**Starship document:**

```javascript
{
    name: "X-Wing",
    pilot_id: ObjectId("123")
}
```

In this example:

* The starship stores the `ObjectId` of the character.
* The actual character data is stored in a separate collection.

### When to use referencing

* When data is large or complex.
* When data is shared across many documents.
* When you want to avoid duplication.

### Advantages

* Reduces duplication of data.
* Easier to maintain consistency.
* Better for large datasets with relationships.

### Disadvantages

* Requires extra queries to fetch related data.
* Slightly more complex to work with.

---

## Embedding vs Referencing Summary

| Feature          | Embedding           | Referencing               |
| ---------------- | ------------------- | ------------------------- |
| Data storage     | Inside document     | Separate collections      |
| Performance      | Faster reads        | Requires multiple queries |
| Data duplication | Higher              | Lower                     |
| Complexity       | Simple              | More complex              |
| Best use case    | Small, related data | Large or shared data      |

---

## Real-world example

* Embedding: A user profile with address details.
* Referencing: A social media user with posts stored in a separate collection.

Choosing between embedding and referencing depends on how the data is used and how often it changes.

## Connecting to MongoDB with Compass

MongoDB Compass is the graphical user interface (GUI) for MongoDB.

To connect to a local MongoDB server:

1. Open MongoDB Compass.
2. Click **Add New Connection**.
3. Enter the connection string:

```text
mongodb://localhost:27017
```

4. Click **Connect**.

Once connected, Compass allows you to create databases, collections, and documents through a user-friendly interface.

## Creating a Database

In MongoDB Shell (mongosh), create or switch to a database using:

```javascript
use sparta
```

MongoDB will create the database automatically when data is first inserted.

## Creating a Collection

A collection is similar to a table in a relational database.

```javascript
db.createCollection("institute")
```

## Adding a Single Document

```javascript
db.institute.insertOne({
    name: "Mohamed Aboudaoud",
    age: 30,
    city: "London"
})
```

## Adding Multiple Documents

```javascript
db.institute.insertMany([
    {
        name: "John Smith",
        age: 25,
        city: "Manchester"
    },
    {
        name: "Sarah Jones",
        age: 28,
        city: "Liverpool"
    }
])
```

## Conclusion

MongoDB is a powerful NoSQL database that stores data in collections and documents rather than tables and rows. Its flexible structure makes it suitable for modern applications that require scalability and adaptability. While it has some disadvantages compared to relational databases, it remains one of the most widely used databases for handling large and evolving datasets.
