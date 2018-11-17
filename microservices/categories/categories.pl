use strict;
use warnings;
use Mojolicious::Lite;
# A Perl Microservice Sample
# perl categories.pl daemon -m production -l http://*:8080

# 
# Setup Routes
#
get '/v1/category/:category_uuid' => 
sub {
    shift->render(
            json => {
                "id" => 1,
                "name" => "Perl",
                "category_uuid" => "1234-1234-1234-1234"
            }
        );
};

put '/v1/category/:category_uuid' =>
sub {
    shift->render(
        text => 'true'
    ); 
};

del '/v1/category/:category_uuid' =>
sub {
    shift->render(
        text => 'true'
    );
};

post '/v1/category' =>
sub {
    shift->render(
        text => 'true'
    );
};

get '/v1/category' => 
sub {
    shift->render(
        json => [
            {
                "id" => 1,
                "name" => "Perl",
                "category_uuid" => "1234-1234-1234-1234"
            },
            {
                "id" => 2,
                "name" => "Python",
                "category_uuid" => "4321-4321-4321-4321"
            }
        ]
    );
};

app->start;
