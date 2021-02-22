---- user

Create table auth (id serial primary key, username varchar(25) unique not null, password varchar(50), last_login timestamp, created_at timestamp, is_active boolean default true);

create table userprofile (id serial primary key, user_id int, CONSTRAINT fk_user foreign key(user_id) REFERENCES auth(id)
,email varchar(250) not null, mobile_number varchar(15)
not null, profile_type varchar(50) not null, profiel_pic varchar(250),
created_at timestamp, updated_at timestamp, is_active boolean default true);

alter table userprofile add constraint user_id unique (user_id);

create table district (id serial primary key, name varchar(50), code varchar(50) unique, is_active boolean default true);

create table state (id serial primary key, name varchar(50), code varchar(50) unique, is_active boolean default true);
alter table state alter column name type varchar(250);
create table state_district (id serial primary key, state_id int, district_id int,
							constraint fk_district foreign key(district_id) references district(id),
					  		constraint fk_state foreign key(state_id) references state(id),
					  		unique(state_id, district_id));

CREATE FUNCTION update_updated_at_column() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
  BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
  END;
$$;
CREATE TRIGGER address_updated_at_modtime BEFORE UPDATE ON address FOR EACH ROW EXECUTE PROCEDURE 
			update_updated_at_column();
create table address (id serial primary key, district_id int, state_id int,
					  constraint fk_district foreign key(district_id) references district(id),
					  constraint fk_state foreign key(state_id) references state(id),
					  address varchar(250), 
					  city varchar(250), 
					  zip_code varchar(25),
					  created_at timestamp default current_timestamp, 
					  updated_at timestamp default current_timestamp,
					  is_active boolean default true);

create table event_category (id serial primary key, name varchar(50), code varchar(50) unique, is_active boolean default true);

create type inquiry_status as enum('Created', 'SendQuery', 'ReceivedQuotation', 'AcceptQuotation', 'Expired')
						  
-- create table inquiry (id serial primary key,
-- 					status inquiry_status,
-- 					query_id varchar (20) unique,
-- 					event_category_id int,
-- 					title text,
-- 					address_id int, 
-- 					extra_message text,
-- 					budget float8 not null default 1.0, 
-- 					from_time timestamp default current_timestamp, 
-- 					to_time timestamp not null, 
-- 					created_at timestamp default current_timestamp, 
-- 					updated_at timestamp default current_timestamp,
-- 					is_active boolean default true,
-- 					created_by_id int,
-- 					metadata jsonb,
-- 					constraint fk_user foreign key(created_by_id) references auth(id),
-- 					constraint fk_enent_category foreign key(event_category_id) references event_category(id)
-- 					);
-- alter table inquiry add constraint fk_address foreign key(address_id) references address(id)

create table inquiry (id serial primary key,
					status inquiry_status,
					query_id varchar (20) unique,
					event_category_id int [],
					title text,
					address_id int, 
					extra_message text,
					budget float8 not null default 1.0, 
					from_time timestamp default current_timestamp, 
					to_time timestamp not null, 
					created_at timestamp default current_timestamp, 
					updated_at timestamp default current_timestamp,
					is_active boolean default true,
					created_by_id int,
					updated_by_id int,
					metadata jsonb,
					constraint fk_created_by foreign key(created_by_id) references auth(id),
					constraint fk_updated_by foreign key(updated_by_id) references auth(id)

					
--					constraint fk_enent_category foreign key(event_category_id) references event_category(id)
					);
--https://www.compose.com/articles/faster-operations-with-the-jsonb-data-type-in-postgresql/

drop table user_group ;
create table "group" (id serial primary key, name varchar(100), code varchar(50));
insert into "group" (name, code) values ('customer', 'C'),('photographer', 'P'), ('admin', 'A');
alter table auth add column group_id int;
alter table auth add constraint fk_group foreign key (group_id) references "group"(id);
create table permission (id serial primary key, name varchar(100), code varchar(50));
create table group_permission (id serial primary key,
								group_id int, constraint fk_group foreign key(group_id) references user_group(id),
							permission_id int, constraint fk_permission foreign key(permission_id) references permission(id)); 


create table quotation_detail (id serial primary key, 
						photographer_id int, constraint photographer_id foreign key(photographer_id) REFERENCES auth(id),
						quote float8 not null default 1.0, 
						message text,
						is_accepted boolean default false,
						created_at timestamp default current_timestamp
						)

create table quotation (id serial primary key,
						inquiry_id int, constraint inquiry_id foreign key(inquiry_id) references inquiry(id),
						quotation_detail_id int, constraint quotation_detail_id foreign key(quotation_detail_id) references quotation_detail(id),
						is_active boolean default true,
						created_at timestamp default current_timestamp
						)

CREATE TRIGGER send_query_updated_at_modtime BEFORE UPDATE ON send_query FOR EACH ROW EXECUTE PROCEDURE 
			update_updated_at_column();
		
create table send_query (id serial primary key, 
						inquiry_id int, constraint inquiry_id foreign key(inquiry_id) references inquiry(id),
						photographer_id int, constraint photographer_id foreign key(photographer_id) REFERENCES auth(id),
						is_active boolean default true,
						created_at timestamp default current_timestamp,
						updated_at timestamp default current_timestamp,
						unique (inquiry_id, photographer_id)
						)

CREATE TRIGGER portfolio_image_updated_at_modtime BEFORE UPDATE ON portfolio_image FOR EACH ROW EXECUTE PROCEDURE 
			update_updated_at_column();
		
create table portfolio_image (id serial primary key, 
								image_path varchar(250),
								created_by_id int,
								updated_by_id int,
								constraint created_by_id foreign key(created_by_id) references auth(id),
								constraint updated_by_id foreign key(updated_by_id) references auth(id),
								created_at timestamp default current_timestamp,
								updated_at timestamp)

create table portfolio_video (id serial primary key, 
								video_path varchar(250),
								created_by_id int,
								updated_by_id int,
								source varchar,
								source_data json,
								constraint created_by_id foreign key(created_by_id) references auth(id),
								constraint updated_by_id foreign key(updated_by_id) references auth(id),
								created_at timestamp default current_timestamp,
								updated_at timestamp)
CREATE TRIGGER portfolio_video_updated_at_modtime BEFORE UPDATE ON portfolio_video FOR EACH ROW EXECUTE PROCEDURE 
			update_updated_at_column();


create table photographer_profile(id serial primary key, user_id int, address_id int, 
								address_proof varchar(250), gst_number varchar(20),
								gst_proof varchar(250), location_availability int [], 
								experties int [], is_active boolean default true, 
								is_verified boolean default false, 
								metadata json,
								constraint user_id foreign key(user_id) references auth(id),
								constraint address_id foreign key(address_id) references address(id),
								created_at timestamp default current_timestamp,
								updated_at timestamp
								)
alter table photographer_profile add constraint unique_user unique (user_id)	;						
						