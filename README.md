# Wiki Stream Data Processing
![alt text](https://github.com/gora050/wiki_data/blob/master/ProjectSystemDiagram.png)

## Usage Category A
1. First you need to install Kafka and Spark on your machine(steps depends on the OS which you use)
2. Start zookeeper, kafka-server and spark standalone cluster or cluster whith multiple slaves
3. Start producer which will post wiki events to kafka topic for at least 6 hours.
4. ```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.6 src/spark_application.py```
5. Go to Flask and try following endpoints:
* user_activity/
* bots_created/
* domain_count/

## Result examples Category A
* Bots Created Endpoint
```json
[{
    "time_start": 16,
    "time_end": 17,
    "statistics": ["{\"domain\":\"id.wikipedia.org\",\"created_by_bots\":10}", "{\"domain\":\"ta.wikipedia.org\",\"created_by_bots\":5}", "{\"domain\":\"mg.wiktionary.org\",\"created_by_bots\":31}", "{\"domain\":\"en.wikipedia.org\",\"created_by_bots\":27}", "{\"domain\":\"ru.wikinews.org\",\"created_by_bots\":3105}", "{\"domain\":\"tr.wikipedia.org\",\"created_by_bots\":120}", "{\"domain\":\"de.wikipedia.org\",\"created_by_bots\":3}", "{\"domain\":\"es.wikipedia.org\",\"created_by_bots\":13}", "{\"domain\":\"ar.wikipedia.org\",\"created_by_bots\":265}", "{\"domain\":\"it.wikipedia.org\",\"created_by_bots\":65}", "{\"domain\":\"ru.wikipedia.org\",\"created_by_bots\":26}", "{\"domain\":\"zh.wikipedia.org\",\"created_by_bots\":27}", "{\"domain\":\"www.wikidata.org\",\"created_by_bots\":430}", "{\"domain\":\"fr.wikipedia.org\",\"created_by_bots\":65}", "{\"domain\":\"as.wikipedia.org\",\"created_by_bots\":2}", "{\"domain\":\"bn.wikipedia.org\",\"created_by_bots\":21}"]
}, {
    "time_start": 18,
    "time_end": 19,
    "statistics": ["{\"domain\":\"meta.wikimedia.org\",\"created_by_bots\":7}", "{\"domain\":\"fr.wikinews.org\",\"created_by_bots\":4}"]
}, {
    "time_start": 20,
    "time_end": 21,
    "statistics": ["{\"domain\":\"my.wikipedia.org\",\"created_by_bots\":4}", "{\"domain\":\"lt.wikipedia.org\",\"created_by_bots\":1}", "{\"domain\":\"ca.wikipedia.org\",\"created_by_bots\":2}"]
}, {
    "time_start": 19,
    "time_end": 20,
    "statistics": ["{\"domain\":\"fa.wikipedia.org\",\"created_by_bots\":1}", "{\"domain\":\"no.wikipedia.org\",\"created_by_bots\":1}", "{\"domain\":\"af.wikipedia.org\",\"created_by_bots\":2}", "{\"domain\":\"uk.wikipedia.org\",\"created_by_bots\":81}"]
}]
```
* Domain Count Endpoint
```json
[{
    "time_start": 21,
    "time_end": 22,
    "statistics": ["{\"domain\":\"su.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"fy.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"es.wikisource.org\",\"domain_number\":1}", "{\"domain\":\"lmo.wikipedia.org\",\"domain_number\":1}"]
}, {
    "time_start": 16,
    "time_end": 17,
    "statistics": ["{\"domain\":\"bh.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"cs.wikipedia.org\",\"domain_number\":52}", "{\"domain\":\"commons.wikimedia.org\",\"domain_number\":3631}", "{\"domain\":\"en.wikinews.org\",\"domain_number\":14}", "{\"domain\":\"ko.wikipedia.org\",\"domain_number\":73}", "{\"domain\":\"id.wikipedia.org\",\"domain_number\":73}", "{\"domain\":\"ta.wikipedia.org\",\"domain_number\":17}", "{\"domain\":\"es.wikinews.org\",\"domain_number\":1}", "{\"domain\":\"vi.wiktionary.org\",\"domain_number\":4}", "{\"domain\":\"mg.wiktionary.org\",\"domain_number\":49}", "{\"domain\":\"en.wikipedia.org\",\"domain_number\":1369}", "{\"domain\":\"ru.wikinews.org\",\"domain_number\":6702}", "{\"domain\":\"kn.wikipedia.org\",\"domain_number\":3}", "{\"domain\":\"da.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"tr.wikisource.org\",\"domain_number\":5}", "{\"domain\":\"it.wikiquote.org\",\"domain_number\":5}", "{\"domain\":\"en.wikisource.org\",\"domain_number\":288}", "{\"domain\":\"sr.wikipedia.org\",\"domain_number\":34}", "{\"domain\":\"fr.wiktionary.org\",\"domain_number\":85}", "{\"domain\":\"tr.wikipedia.org\",\"domain_number\":238}", "{\"domain\":\"bg.wikipedia.org\",\"domain_number\":15}", "{\"domain\":\"zh.wiktionary.org\",\"domain_number\":16}", "{\"domain\":\"cy.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"gu.wikisource.org\",\"domain_number\":12}", "{\"domain\":\"be-tarask.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"incubator.wikimedia.org\",\"domain_number\":63}", "{\"domain\":\"hyw.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"uk.wiktionary.org\",\"domain_number\":3}", "{\"domain\":\"he.wikipedia.org\",\"domain_number\":54}", "{\"domain\":\"nap.wikisource.org\",\"domain_number\":10}", "{\"domain\":\"fr.wikisource.org\",\"domain_number\":143}", "{\"domain\":\"de.wikipedia.org\",\"domain_number\":222}", "{\"domain\":\"fr.wikiquote.org\",\"domain_number\":3}", "{\"domain\":\"pt.wikipedia.org\",\"domain_number\":90}", "{\"domain\":\"es.wikipedia.org\",\"domain_number\":207}", "{\"domain\":\"fr.wikiversity.org\",\"domain_number\":4}", "{\"domain\":\"eu.wikipedia.org\",\"domain_number\":27}", "{\"domain\":\"hy.wikipedia.org\",\"domain_number\":32}", "{\"domain\":\"ar.wikipedia.org\",\"domain_number\":438}", "{\"domain\":\"lez.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"ro.wikipedia.org\",\"domain_number\":35}", "{\"domain\":\"el.wiktionary.org\",\"domain_number\":7}", "{\"domain\":\"ca.wikisource.org\",\"domain_number\":5}", "{\"domain\":\"de.wiktionary.org\",\"domain_number\":122}", "{\"domain\":\"sk.wikipedia.org\",\"domain_number\":14}", "{\"domain\":\"fa.wikipedia.org\",\"domain_number\":136}", "{\"domain\":\"it.wikipedia.org\",\"domain_number\":347}", "{\"domain\":\"gu.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"nl.wikipedia.org\",\"domain_number\":54}", "{\"domain\":\"arz.wikipedia.org\",\"domain_number\":796}", "{\"domain\":\"pl.wikipedia.org\",\"domain_number\":170}", "{\"domain\":\"ru.wiktionary.org\",\"domain_number\":19}", "{\"domain\":\"meta.wikimedia.org\",\"domain_number\":145}", "{\"domain\":\"nl.wiktionary.org\",\"domain_number\":9}", "{\"domain\":\"ia.wiktionary.org\",\"domain_number\":21}", "{\"domain\":\"th.wikipedia.org\",\"domain_number\":228}", "{\"domain\":\"hu.wikipedia.org\",\"domain_number\":19}", "{\"domain\":\"id.wiktionary.org\",\"domain_number\":1}", "{\"domain\":\"sv.wikipedia.org\",\"domain_number\":33}", "{\"domain\":\"et.wiktionary.org\",\"domain_number\":5}", "{\"domain\":\"ja.wikipedia.org\",\"domain_number\":75}", "{\"domain\":\"hi.wikipedia.org\",\"domain_number\":71}", "{\"domain\":\"ur.wikipedia.org\",\"domain_number\":15}", "{\"domain\":\"ru.wikipedia.org\",\"domain_number\":227}", "{\"domain\":\"uk.wikipedia.org\",\"domain_number\":1793}", "{\"domain\":\"zh.wikipedia.org\",\"domain_number\":150}", "{\"domain\":\"www.wikidata.org\",\"domain_number\":1378}", "{\"domain\":\"fr.wikipedia.org\",\"domain_number\":456}", "{\"domain\":\"ru.wikisource.org\",\"domain_number\":29}", "{\"domain\":\"species.wikimedia.org\",\"domain_number\":104}", "{\"domain\":\"ro.wikisource.org\",\"domain_number\":2}", "{\"domain\":\"mdf.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"sh.wikipedia.org\",\"domain_number\":6}", "{\"domain\":\"de.wikiversity.org\",\"domain_number\":8}", "{\"domain\":\"fy.wiktionary.org\",\"domain_number\":1}", "{\"domain\":\"nds.wikipedia.org\",\"domain_number\":9}", "{\"domain\":\"simple.wikipedia.org\",\"domain_number\":26}", "{\"domain\":\"az.wikipedia.org\",\"domain_number\":16}", "{\"domain\":\"scn.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"ca.wikipedia.org\",\"domain_number\":102}", "{\"domain\":\"sl.wiktionary.org\",\"domain_number\":1}", "{\"domain\":\"as.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"ne.wikipedia.org\",\"domain_number\":6}", "{\"domain\":\"sv.wikisource.org\",\"domain_number\":1}", "{\"domain\":\"hr.wikipedia.org\",\"domain_number\":7}", "{\"domain\":\"bn.wikipedia.org\",\"domain_number\":64}", "{\"domain\":\"en.wiktionary.org\",\"domain_number\":260}"]
}, {
    "time_start": 18,
    "time_end": 19,
    "statistics": ["{\"domain\":\"ce.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"et.wikipedia.org\",\"domain_number\":12}", "{\"domain\":\"mk.wikipedia.org\",\"domain_number\":9}", "{\"domain\":\"kk.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"el.wikipedia.org\",\"domain_number\":16}", "{\"domain\":\"sl.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"eo.wikisource.org\",\"domain_number\":1}", "{\"domain\":\"wikisource.org\",\"domain_number\":4}", "{\"domain\":\"et.wikiquote.org\",\"domain_number\":2}", "{\"domain\":\"is.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"ku.wiktionary.org\",\"domain_number\":6}", "{\"domain\":\"nds-nl.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"uk.wikisource.org\",\"domain_number\":6}", "{\"domain\":\"la.wikisource.org\",\"domain_number\":2}", "{\"domain\":\"ka.wikipedia.org\",\"domain_number\":49}", "{\"domain\":\"myv.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"bn.wiktionary.org\",\"domain_number\":4}", "{\"domain\":\"pl.wiktionary.org\",\"domain_number\":12}", "{\"domain\":\"it.wikivoyage.org\",\"domain_number\":5}", "{\"domain\":\"nv.wikipedia.org\",\"domain_number\":11}", "{\"domain\":\"sat.wikipedia.org\",\"domain_number\":5}", "{\"domain\":\"sr.wiktionary.org\",\"domain_number\":92}", "{\"domain\":\"ja.wiktionary.org\",\"domain_number\":14}", "{\"domain\":\"es.wikivoyage.org\",\"domain_number\":2}", "{\"domain\":\"it.wikisource.org\",\"domain_number\":19}", "{\"domain\":\"gl.wikipedia.org\",\"domain_number\":9}", "{\"domain\":\"az.wiktionary.org\",\"domain_number\":1}", "{\"domain\":\"be.wikipedia.org\",\"domain_number\":18}", "{\"domain\":\"fr.wikinews.org\",\"domain_number\":6}", "{\"domain\":\"lv.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"la.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"mai.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"th.wiktionary.org\",\"domain_number\":1}", "{\"domain\":\"zh-classical.wikipedia.org\",\"domain_number\":3}", "{\"domain\":\"fa.wiktionary.org\",\"domain_number\":8}", "{\"domain\":\"vi.wikipedia.org\",\"domain_number\":34}", "{\"domain\":\"fi.wikipedia.org\",\"domain_number\":15}", "{\"domain\":\"it.wiktionary.org\",\"domain_number\":3}", "{\"domain\":\"zh-yue.wikipedia.org\",\"domain_number\":25}", "{\"domain\":\"udm.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"mn.wikipedia.org\",\"domain_number\":2}"]
}, {
    "time_start": 20,
    "time_end": 21,
    "statistics": ["{\"domain\":\"pt.wikisource.org\",\"domain_number\":45}", "{\"domain\":\"bar.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"ru.wikiquote.org\",\"domain_number\":2}", "{\"domain\":\"azb.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"pnb.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"tl.wikipedia.org\",\"domain_number\":3}", "{\"domain\":\"my.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"cs.wiktionary.org\",\"domain_number\":5}", "{\"domain\":\"li.wikipedia.org\",\"domain_number\":1}", "{\"domain\":\"cs.wikiversity.org\",\"domain_number\":1}", "{\"domain\":\"pt.wiktionary.org\",\"domain_number\":2}"]
}, {
    "time_start": 17,
    "time_end": 18,
    "statistics": ["{\"domain\":\"bs.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"eo.wikipedia.org\",\"domain_number\":36}", "{\"domain\":\"ast.wikipedia.org\",\"domain_number\":5}", "{\"domain\":\"pl.wikisource.org\",\"domain_number\":33}"]
}, {
    "time_start": 19,
    "time_end": 20,
    "statistics": ["{\"domain\":\"tyv.wikipedia.org\",\"domain_number\":3}", "{\"domain\":\"ga.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"it.wikiversity.org\",\"domain_number\":1}", "{\"domain\":\"ku.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"ml.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"tr.wiktionary.org\",\"domain_number\":1}", "{\"domain\":\"kn.wikisource.org\",\"domain_number\":1}", "{\"domain\":\"pa.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"de.wikisource.org\",\"domain_number\":13}", "{\"domain\":\"test2.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"www.mediawiki.org\",\"domain_number\":131}", "{\"domain\":\"lt.wikipedia.org\",\"domain_number\":10}", "{\"domain\":\"tt.wikipedia.org\",\"domain_number\":148}", "{\"domain\":\"vep.wikipedia.org\",\"domain_number\":3}", "{\"domain\":\"no.wikipedia.org\",\"domain_number\":20}", "{\"domain\":\"af.wikipedia.org\",\"domain_number\":7}", "{\"domain\":\"lad.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"sco.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"bd.wikimedia.org\",\"domain_number\":1}", "{\"domain\":\"ms.wikipedia.org\",\"domain_number\":1128}", "{\"domain\":\"br.wikipedia.org\",\"domain_number\":2}", "{\"domain\":\"hi.wikiquote.org\",\"domain_number\":1}", "{\"domain\":\"ta.wikisource.org\",\"domain_number\":5}", "{\"domain\":\"fi.wiktionary.org\",\"domain_number\":2}", "{\"domain\":\"ky.wiktionary.org\",\"domain_number\":2}", "{\"domain\":\"diq.wikipedia.org\",\"domain_number\":62}", "{\"domain\":\"sq.wikipedia.org\",\"domain_number\":4}", "{\"domain\":\"io.wiktionary.org\",\"domain_number\":4}", "{\"domain\":\"oc.wikipedia.org\",\"domain_number\":4}"]
}]
```
* User acitvity
File is to big so we added it to the repository.
Some files have bad encoding so sorry for the bytes in the text :(

## Usage Category B

1.Install minikube & kubectl & docker
2. Repeat Steps from Cat. A, to start gathering data
3. Use "./run b" - to build docker images
4. Use "./run" - to start k3s pods ("./run stop" - to stop)
5. 0.0.0.0:8090 - Use for testing API UI and Json api
PS. use kubectl to browse logs, etc (we use local namespace)
PPS. Pods of API layer could easily be scaled, if needed. As well as Postgres supports replication 
 
## Result examples Category B

* All sample results & queries are presented as screenshots in /api_samples folder