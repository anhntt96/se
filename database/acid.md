From book: Designing Data-Intensive Applications

ACID stand for Atomicity, Consitency, Isolation and Durabiity.

System that do not meet the ACID criteria are sometimes called BASE, which stands for Basically Available, Soft state, and Eventual consistency.

### Atomicity
- Ingeneral, atomicity refers to something that can not be broken down into smaller parts.

- Atomicity describes what happens if a client wants to make several writes, but a fault occurs after some of the writes have been processed. If the writes are grouped together into an atomic transaction, and the transaction cannot be completed due to a fault, then the transaction is aborted and the database must discard or undo any writes it has made so far in that transaction.


### Consistency
- In the context of ACID, consistency refers to an application-specific notion of the database being in a "good state".
- The idea of ACID consistency is that you have certain statements about your data that must always be true - for example, in an accounting system, credits and debits across all accounts must always be balanced. 
- However, this idea of consistency depends on the application. This is not something that the database can guarantee: if you write bad data that violates your invariants, the database can not stop you. 
- Some specific kinds of invariants can be checked by the database, for example using foreign key constraints or uniqueness constraints. However, in general, the application defines what data is valid or invalid - the database only stores it.
  
### Isolation
- Most databases are accessed by several clients at the same time. If they are accessing the same database records, you can run into concurrency problems. (race condition)
- Isolation means that concurrently executing transactions are isolated from each other: they can not step on each other's toes.

### Durability
- The purpose of a database system is to provide a safe place where data can be stored without fear of losing it. 
- Durability is the promise that once a transaction has committed successfully, any data it has written will not be forgotten, even if there is a hardware fault or the database crashes.
- In a single-node database, durability typically means that the data has been written to nonvolatile storage such as a hard drive or SSD. 
- In a replicated database, durability may mean that the data has been successfully copied to some number of nodes. In order to provide a durability guarantee, a database must wait until these writes or replications are complete before reporting a transaction as successfully committed.