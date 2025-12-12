---
tags:
  - Reference
---

# Data tables

```
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |
```

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

## Column alignment

=== "Left"

    ```
    | Method      | Description                          |
    | :---------- | :----------------------------------- |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ```
    
    | Method      | Description                          |
    | :---------- | :----------------------------------- |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |

=== "Center"

    ```
    | Method      | Description                          |
    | :---------: | :----------------------------------: |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ```

    | Method      | Description                          |
    | :---------: | :----------------------------------: |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |

=== "Right"

    ```
    | Method      | Description                          |
    | ----------: | -----------------------------------: |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ```
    
    | Method      | Description                          |
    | ----------: | -----------------------------------: |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |

## HTML

```
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
</table>
```
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
</table>

## Import table from file
***

=== "Import data from :fontawesome-solid-file-csv: CSV file"
    
    Let's use a :fontawesome-solid-file-csv: CSV in the local directory. The file may look like this:

    ```csv title="./data.csv"
    col1,col2,col3
    r1c1,r1c2,r1c3
    r2c1,r2c2,r2c3
    r3c1,r3c2,r3c3
    ```

    You can then add it to your :fontawesome-solid-file-arrow-down: Markdown page like this:

    ```md title="./markdown.md"
    ...

    {{ read_csv('./data/data.csv') }}

    ...
    ```

    <div class="result" markdown>

    ...

    col1|col2|col3
    ----|----|----
    r1c1|r1c2|r1c3
    r2c1|r2c2|r2c3
    r3c1|r3c2|r3c3

    ...

    </div>

=== "Import data from other file types"

    The plugin [`mkdocs-table-reader-plugin`][table-reader-docs] also provides readers for other formats:

    <div class="mdx-columns" markdown>

    - [`read_csv`][table-reader-read_csv]
    - [`read_fwf`][table-reader-read_fwf]
    - [`read_yaml`][table-reader-read_yaml]
    - [`read_table`][table-reader-read_table]
    - [`read_json`][table-reader-read_json]
    - [`read_excel`][table-reader-read_excel]
    - [`read_raw`][table-reader-read_raw]

    </div>

    You can read more on their Docs website: [mkdocs-table-reader-plugin][table-reader-docs]

[table-reader-docs]: https://timvink.github.io/mkdocs-table-reader-plugin/
[table-reader-read_csv]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_csv
[table-reader-read_fwf]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_fwf
[table-reader-read_yaml]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_yaml
[table-reader-read_table]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_table
[table-reader-read_json]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_json
[table-reader-read_excel]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_excel
[table-reader-read_raw]: https://timvink.github.io/mkdocs-table-reader-plugin/readers/#read_raw
