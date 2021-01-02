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
						  
create table inquiry (id serial primary key,
					status inquiry_status,
					query_id varchar (20) unique,
					event_category_id int,
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
					metadata jsonb,
					constraint fk_user foreign key(created_by_id) references auth(id),
					constraint fk_enent_category foreign key(event_category_id) references event_category(id)
					);
alter table inquiry add constraint fk_address foreign key(address_id) references address(id)
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