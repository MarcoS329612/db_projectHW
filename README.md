# 🎬 DB_PROJECTHW

Este proyecto escolar fue desarrollado utilizando **Python 3.12** con una estructura modular. Las interfaces gráficas fueron diseñadas con **Tkinter**, y se utiliza **SQL Server** como base de datos, conectada mediante la biblioteca **pyodbc**.

---

## 📚 Tabla de Contenidos

1. [📖 Descripción del Proyecto](#📖-descripción-del-proyecto)
2. [💻 Requisitos Previos](#💻-requisitos-previos)
3. [⚙️ Instalación](#⚙️-instalación)
4. [📂 Estructura del Proyecto](#📂-estructura-del-proyecto)
5. [🚀 Funcionamiento](#🚀-funcionamiento)
6. [🤝 Contribuciones](#🤝-contribuciones)

---

## 📖 Descripción del Proyecto

El propósito de este proyecto es simular un sistema de selección de películas, registro de usuarios y compra de boletos. Es una aplicación modular que permite:

- 📝 Registro de usuarios.
- 🔑 Inicio de sesión de usuarios registrados.
- 🎥 Selección de películas y horarios.
- 🎟️ Confirmación de boletos.

Se desarrolló como un proyecto académico para demostrar el uso de bases de datos SQL Server en combinación con interfaces gráficas en Python.

---

## 💻 Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- 🐍 **Python 3.12**
- 🗄️ **SQL Server** (configurado y con acceso)
- 📦 **pip** para la instalación de dependencias

---

## ⚙️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/MarcoS329612/db_projectHW.git
   cd DB_PROJECTHW

2. Crea un entorno virtual:
   ```bash
    python -m venv .venv
    source .venv/bin/activate   # En Windows: .venv\Scripts\activate

3. Instala las dependedncias del proyecto:
   ```bash
   pip install -r requirements.txt

4. Configura la conexión a SQL Server en el archivo connection.py



El Script de la base de datos es el siguiente

   ```bash

   
   USE [CineDB]
   GO
   /****** Object:  Table [dbo].[Boletos]    Script Date: 29/11/2024 03:08:14 a. m. ******/
   SET ANSI_NULLS ON
   GO
   SET QUOTED_IDENTIFIER ON
   GO
   CREATE TABLE [dbo].[Boletos](
   	[BoletoID] [int] IDENTITY(1,1) NOT NULL,
   	[FuncionID] [int] NOT NULL,
   	[UsuarioID] [int] NOT NULL,
   	[FechaVenta] [datetime] NULL,
   	[Precio] [decimal](10, 2) NOT NULL,
   PRIMARY KEY CLUSTERED 
   (
   	[BoletoID] ASC
   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
   ) ON [PRIMARY]
   GO
   /****** Object:  Table [dbo].[Funciones]    Script Date: 29/11/2024 03:08:14 a. m. ******/
   SET ANSI_NULLS ON
   GO
   SET QUOTED_IDENTIFIER ON
   GO
   CREATE TABLE [dbo].[Funciones](
   	[FuncionID] [int] IDENTITY(1,1) NOT NULL,
   	[PeliculaID] [int] NOT NULL,
   	[SalaID] [int] NOT NULL,
   	[Horario] [datetime] NOT NULL,
   PRIMARY KEY CLUSTERED 
   (
   	[FuncionID] ASC
   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
   ) ON [PRIMARY]
   GO
   /****** Object:  Table [dbo].[Peliculas]    Script Date: 29/11/2024 03:08:14 a. m. ******/
   SET ANSI_NULLS ON
   GO
   SET QUOTED_IDENTIFIER ON
   GO
   CREATE TABLE [dbo].[Peliculas](
   	[PeliculaID] [int] IDENTITY(1,1) NOT NULL,
   	[Titulo] [varchar](150) NOT NULL,
   	[Clasificacion] [varchar](20) NOT NULL,
   	[Duracion] [int] NOT NULL,
   	[Sinopsis] [text] NULL,
   	[FechaEstreno] [date] NULL,
   	[Genero] [varchar](50) NULL,
   PRIMARY KEY CLUSTERED 
   (
   	[PeliculaID] ASC
   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
   ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
   GO
   /****** Object:  Table [dbo].[Salas]    Script Date: 29/11/2024 03:08:14 a. m. ******/
   SET ANSI_NULLS ON
   GO
   SET QUOTED_IDENTIFIER ON
   GO
   CREATE TABLE [dbo].[Salas](
   	[SalaID] [int] IDENTITY(1,1) NOT NULL,
   	[Capacidad] [int] NOT NULL,
   	[TipoSala] [varchar](50) NOT NULL,
   	[Precio] [decimal](10, 2) NULL,
   PRIMARY KEY CLUSTERED 
   (
   	[SalaID] ASC
   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
   ) ON [PRIMARY]
   GO
   /****** Object:  Table [dbo].[Usuarios]    Script Date: 29/11/2024 03:08:14 a. m. ******/
   SET ANSI_NULLS ON
   GO
   SET QUOTED_IDENTIFIER ON
   GO
   CREATE TABLE [dbo].[Usuarios](
   	[UsuarioID] [int] IDENTITY(1,1) NOT NULL,
   	[Nombre] [varchar](100) NOT NULL,
   	[Correo] [varchar](100) NOT NULL,
   	[Contraseña] [varchar](255) NOT NULL,
   	[FechaRegistro] [datetime] NULL,
   PRIMARY KEY CLUSTERED 
   (
   	[UsuarioID] ASC
   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
   UNIQUE NONCLUSTERED 
   (
   	[Correo] ASC
   )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
   ) ON [PRIMARY]
   GO
   ALTER TABLE [dbo].[Boletos] ADD  DEFAULT (getdate()) FOR [FechaVenta]
   GO
   ALTER TABLE [dbo].[Salas] ADD  DEFAULT ('2D') FOR [TipoSala]
   GO
   ALTER TABLE [dbo].[Usuarios] ADD  DEFAULT (getdate()) FOR [FechaRegistro]
   GO
   ALTER TABLE [dbo].[Boletos]  WITH CHECK ADD FOREIGN KEY([FuncionID])
   REFERENCES [dbo].[Funciones] ([FuncionID])
   GO
   ALTER TABLE [dbo].[Boletos]  WITH CHECK ADD FOREIGN KEY([UsuarioID])
   REFERENCES [dbo].[Usuarios] ([UsuarioID])
   GO
   ALTER TABLE [dbo].[Funciones]  WITH CHECK ADD FOREIGN KEY([PeliculaID])
   REFERENCES [dbo].[Peliculas] ([PeliculaID])
   GO
   ALTER TABLE [dbo].[Funciones]  WITH CHECK ADD FOREIGN KEY([SalaID])
   REFERENCES [dbo].[Salas] ([SalaID])
   GO
   
   
