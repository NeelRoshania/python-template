   use database example_warehouse;

   -- create schema example_schema;
   -- create schema example_schema_tst;

   use schema example_schema;
   -- use schema example_schema_tst;
   
   -- drop table example_table;
   -- drop sequence example_sequence_id;
   
   create sequence example_sequence_id;

   create table example_table

   (
      row_insert_timestamp timestamp_ntz not null default current_timestamp,
      record_id number not null default example_sequence_id.nextval, 
      job_id number not null,
      mem_id number,
      mex_id number,
      data_source varchar(15) not null,
      full_name varchar(256),
      work_phone varchar(64),
      work_email varchar(256),
      dozi_company_id number,
      job_title varchar(256),
      linkedin_url varchar(512) not null,
      country varchar(256),
      city varchar(256),
      state varchar(128),
      region varchar(128),
      zip varchar(128),
      industry varchar(128),
      is_eu boolean,
      employment_date_from date,
      employment_date_to date,
      privacy_notice_provided_type varchar(512),
      privacy_notice_provided_date timestamp,
      infusion_status varchar(64) not null default 'INGESTION_SCHEMA_VERIFIED',
      infusion_status_change_date timestamp not null default current_timestamp
   );

   comment on table example_table IS 'Summary of table.';

   comment on COLUMN example_table.infusion_status_change_date IS 'Date of the last status change.';
   comment on COLUMN example_table.data_source IS 'AWK | WDOD | XING | RIPPLE | VENDOR';

   comment on COLUMN example_table.infusion_status IS 'INGESTION_SCHEMA_VERIFIED | HEADER_TITLE_PROCESSED | EMAIL_VERIFIED_NEVERBOUNCE | INFUSED | FAILED';
   comment on COLUMN example_table.row_insert_timestamp IS 'Date the record was added.';
   comment on COLUMN example_table.job_id IS 'Reference that uniquely identifies the batch this record originated from.';
   comment on COLUMN example_table.record_id IS 'Unique ID for each record.';
   comment on COLUMN example_table.full_name IS '{"header":"full_name", "infusion_types":["insert", "update"], "desc":"<full_name>"}';
   comment on COLUMN example_table.work_phone IS '{"header":"work phone", "infusion_types":["insert", "update"], "desc":"<work phone>"}';
   comment on COLUMN example_table.work_email IS '{"header":"work email", "infusion_types":["insert", "update"], "desc":"<work email>"}';
   comment on COLUMN example_table.dozi_company_id IS '{"header":"company id", "infusion_types":["insert", "update"], "desc":"<company id>"}';
   comment on COLUMN example_table.job_title IS '{"header":"job title", "infusion_types":["insert", "update"], "desc":"<title>"}';
   comment on COLUMN example_table.linkedin_url IS '{"header":"LinkedIn URLs", "infusion_types":["insert", "update"], "desc":"<comma-separated LinkedIn URLs>"}';
   comment on COLUMN example_table.country IS '{"header":"Street", "infusion_types":["insert", "update"], "desc":"<street>"}';
   comment on COLUMN example_table.city IS '{"header":"City", "infusion_types":["insert", "update"], "desc":"<city>"}';
   comment on COLUMN example_table.state IS '{"header":"State", "infusion_types":["insert", "update"], "desc":"<state>"}';
   comment on COLUMN example_table.region IS '{"header":"Region", "infusion_types":["insert", "update"], "desc":"<Region>"}';
   comment on COLUMN example_table.zip IS '{"header":"Zip", "infusion_types":["insert", "update"], "desc":"<Zip>"}';
   comment on COLUMN example_table.industry IS '{"header":"Industry", "infusion_types":["insert", "update"], "desc":"<Industry>"}';
   comment on COLUMN example_table.is_eu IS '{"header":"is_eu", "infusion_types":["insert", "update"], "desc":"<is_eu>"}';
   comment on COLUMN example_table.privacy_notice_provided_type IS '{"header":"Privacy Notice Provided Type", "infusion_types":["insert", "update"], "desc":"<EMAIL_TO_BUSINESS_EMAIL | EMAIL_TO_PERSONAL_EMAIL | RECORDED_CALL_TO_BUSINESS_PHONE | TEXT_MESSAGE_TO_MOBILE_PHONE | POSTCARD_TO_BUSINESS_ADDRESS>"}';
   comment on COLUMN example_table.privacy_notice_provided_date IS '{"header":"Privacy Notice Provided Date", "infusion_types":["insert", "update"], "desc":"<privacy_notice_provided_date>"}';
