## MongoDB Documentation

### MongoDB Commands

**Create Database**

```bash
> use practicedb
```


**Current Active Database**
```bash
> db
```

**Show Databases**

```bash
> show dbs
```

**Insert Data**

```bash
> db.zoo.insert({name: 'Cleo', species: 'jaguar', age: 12, hobbies: ['sleeping', 'eating', 'climbing']})
```

**Show collections**

```bash
> show collections
```

**View contents of Collection**

```bash
> db.zoo.find()
```

**Delete document**

```bash
> db.zoo.remove({name: 'Cleo'})
```

**Remove entire collection**

```bash
> db.zoo.drop()
```

**Drop database**

```bash
> db.dropDatabase()
```




