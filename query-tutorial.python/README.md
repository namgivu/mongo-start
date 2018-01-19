info 0th
===

DOING ref. https://docs.mongodb.com/manual/tutorial/query-documents/
  all compare operator
  ref. https://docs.mongodb.com/manual/reference/operator/query-comparison/#query-selectors-comparison
  all operators
  ref. https://docs.mongodb.com/manual/reference/operator/query/
TODO sql vs mongo syntax
ref. https://docs.mongodb.com/manual/reference/sql-comparison/


---


mongo .aggregate()
===

TODO Some accumulators are available in the $project stage; however, when used in the $project stage, the accumulators do not maintain their state across documents.
ref. https://docs.mongodb.com/manual/core/aggregation-pipeline/#pipeline-expressions
NOTE To optimize the operation, wherever possible, use the following strategies to avoid scanning the entire collection
ref. https://docs.mongodb.com/manual/core/aggregation-pipeline/#aggregation-pipeline-behavior
  > The **$match and $sort** pipeline operators can
    take advantage of an index when they occur at the **beginning of the pipeline**
  > Make use of **early filtering** via $match
  > more optimized ref. https://docs.mongodb.com/manual/core/aggregation-pipeline-optimization/
  > use sharding   ref. https://docs.mongodb.com/manual/core/aggregation-pipeline-sharded-collections/#aggregation-pipeline-sharded-collection
Since 2.6, aggregate command can return either a cursor or **store the results in a collection**
ref. https://docs.mongodb.com/manual/core/aggregation-pipeline-limits/
About pipeline
  ref. https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/#aggregation-pipeline-stages
  documents pass through the stages **in sequence**
  ```
  db.collection.aggregate( pipeline                  )
  db.collection.aggregate( [ stage00, stage01, ... ] )
  stageXX in [$match
              $project $addFields
              $group
              $sort $sortByCount
              $count
              $limit
              $skip
              $out                   //output result to a collection - must be the LAST STAGE in the pipeline

              
              //the understood
              $bucket $bucketAuto    //grouping
              $facet                 //aggregation within a stage
              $lookup                //left-join with another collection
              $sample                //return random number of rows
              $redact                //incorporates the functionality of $project and $match; eg. used ffor field level redaction
              $replaceRoot           //replace current doc by another embeded doc

              //the not-understood
              $collStats $indexStats
              $currentOp
              $geoNear $graphLookup
              $listLocalSessions $listSessions
              $unwind
  ]
  ```
  
  TODO diff. betw. $addFields vs. $project
     $addFields  just add new fields to current field set
     $project    can add or remove aka. resharpe
     
  TODO diff. betw. $bucketXX vs. $group
  