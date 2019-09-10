USE smart_lift ;

CREATE TABLE IF NOT EXISTS lift (lift_id INT NOT NULL PRIMARY KEY, floor_id INT, building_id INT, out_of_order INT ); 