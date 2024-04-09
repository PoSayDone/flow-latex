conversation_participant = Table(
    "conversation_participant",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("conversation_id", ForeignKey("conversations.id"), primary_key=True),
)

user_interest_table = Table(
    "user_interest",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("users.id"), primary_key=True),
    Column("interest_id", Integer, ForeignKey("interests.id"), primary_key=True),
)

user_trip_purpose_table = Table(
    "user_trip_purpose",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("users.id"), primary_key=True),
    Column(
        "trip_purpose_id", Integer, ForeignKey("trip_purposes.id"), primary_key=True
    ),
)

user_departure_table = Table(
    "user_departure",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("users.id"), primary_key=True),
    Column("departure_id", Integer, ForeignKey("departures.id"), primary_key=True),
)

user_arrival_table = Table(
    "user_arrival",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("users.id"), primary_key=True),
    Column("arrival_id", Integer, ForeignKey("arrivals.id"), primary_key=True),
)


class Users(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, index=True)
    occupation = Column(String, index=True)
    about = Column(String, index=True)
    mail = Column(String, index=True)
    password_hash = Column(String)
    sex = Column(Boolean)
    birthdate = Column(Date)
    registration_date = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    conversations: Mapped[List["Conversation"]] = relationship(
        secondary=conversation_participant, back_populates="users"
    )
    interests: Mapped[List["Interests"]] = relationship(
        "Interests", secondary=user_interest_table, back_populates="users"
    )
    trip_purposes: Mapped[List["TripPurposes"]] = relationship(
        "TripPurposes", secondary=user_trip_purpose_table, back_populates="users"
    )
    departures: Mapped[List["Departures"]] = relationship(
        "Departures", secondary=user_departure_table, back_populates="users"
    )
    arrivals: Mapped[List["Arrivals"]] = relationship(
        "Arrivals", secondary=user_arrival_table, back_populates="users"
    )
    messages: Mapped[List["Message"]] = relationship(back_populates="sender")
    status = Column(Boolean, default=True)
    user_image: Mapped[str] = mapped_column(String(1048), nullable=True)


class RefreshTokens(Base):
    __tablename__ = "refresh_tokens"
    user_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    refresh_token = Column(String)
    expires_at = Column(DateTime)


class Matches(Base):
    __tablename__ = "matches"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    liked_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    mutual = Column(Boolean, default=False)


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, index=True)


class Interests(Base):
    __tablename__ = "interests"
    id = Column(Integer, primary_key=True, autoincrement=True)
    interest_name = Column(String, index=True)
    users = relationship(
        "Users", secondary=user_interest_table, back_populates="interests"
    )


class TripPurposes(Base):
    __tablename__ = "trip_purposes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    purpose_name = Column(String, index=True)
    users = relationship(
        "Users", secondary=user_trip_purpose_table, back_populates="trip_purposes"
    )


class Departures(Base):
    __tablename__ = "departures"
    id = Column(Integer, primary_key=True, autoincrement=True)
    departure_name = Column(String, index=True)
    users = relationship(
        "Users", secondary=user_departure_table, back_populates="departures"
    )


class Arrivals(Base):
    __tablename__ = "arrivals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    arrival_name = Column(String, index=True)
    users = relationship(
        "Users", secondary=user_arrival_table, back_populates="arrivals"
    )


class UsersRoles(Base):
    __tablename__ = "users_roles"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())
    is_deleted = Column(Boolean, default=False)

    users: Mapped[List["Users"]] = relationship(
        secondary=conversation_participant, back_populates="conversations"
    )
    messages: Mapped[List["Message"]] = relationship(back_populates="conversation")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String)
    image = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())

    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    conversation: Mapped["Conversation"] = relationship(back_populates="messages")

    sender_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    sender: Mapped["Users"] = relationship(back_populates="messages")
