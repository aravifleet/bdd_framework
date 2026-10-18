create DATABASE if not EXISTS qa_automation;

use qa_automation;

create table if not exists ui_test_results (
    id int auto_increment PRIMARY KEY,
    test_name varchar(255) not null,
    test_status varchar(200) not null,
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    error_message TEXT
)