namespace PiSync.Room
{
    partial class RoomForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            label2 = new Label();
            tbSearch = new TextBox();
            label3 = new Label();
            btnNewRoom = new Button();
            lblEmpty = new Label();
            dataGridViewRooms = new DataGridView();
            panel3 = new Panel();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewRooms).BeginInit();
            panel3.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(label2);
            panel1.Controls.Add(tbSearch);
            panel1.Controls.Add(label3);
            panel1.Controls.Add(btnNewRoom);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Margin = new Padding(5, 4, 5, 4);
            panel1.Name = "panel1";
            panel1.Size = new Size(875, 79);
            panel1.TabIndex = 1;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 10F);
            label2.ForeColor = Color.Lavender;
            label2.Location = new Point(490, 9);
            label2.Name = "label2";
            label2.Size = new Size(79, 20);
            label2.TabIndex = 7;
            label2.Text = "SEARCH:";
            // 
            // tbSearch
            // 
            tbSearch.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            tbSearch.BackColor = Color.Lavender;
            tbSearch.Location = new Point(490, 32);
            tbSearch.Name = "tbSearch";
            tbSearch.Size = new Size(225, 34);
            tbSearch.TabIndex = 6;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 16F);
            label3.ForeColor = Color.Lavender;
            label3.Location = new Point(59, 24);
            label3.Margin = new Padding(5, 0, 5, 0);
            label3.Name = "label3";
            label3.Size = new Size(93, 30);
            label3.TabIndex = 0;
            label3.Text = "ROOMS";
            // 
            // btnNewRoom
            // 
            btnNewRoom.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnNewRoom.BackColor = Color.Lavender;
            btnNewRoom.FlatAppearance.BorderSize = 0;
            btnNewRoom.FlatStyle = FlatStyle.Flat;
            btnNewRoom.Location = new Point(729, 24);
            btnNewRoom.Name = "btnNewRoom";
            btnNewRoom.Size = new Size(121, 43);
            btnNewRoom.TabIndex = 5;
            btnNewRoom.Text = "NEW";
            btnNewRoom.UseVisualStyleBackColor = false;
            // 
            // lblEmpty
            // 
            lblEmpty.AutoSize = true;
            lblEmpty.BackColor = Color.Lavender;
            lblEmpty.Font = new Font("Courier New", 16F);
            lblEmpty.ForeColor = Color.MediumPurple;
            lblEmpty.Location = new Point(324, 171);
            lblEmpty.Margin = new Padding(5, 0, 5, 0);
            lblEmpty.Name = "lblEmpty";
            lblEmpty.Size = new Size(221, 30);
            lblEmpty.TabIndex = 3;
            lblEmpty.Text = "NO ROOMS YET.";
            // 
            // dataGridViewRooms
            // 
            dataGridViewRooms.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            dataGridViewRooms.BackgroundColor = Color.Lavender;
            dataGridViewRooms.BorderStyle = BorderStyle.None;
            dataGridViewRooms.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewRooms.Location = new Point(19, 20);
            dataGridViewRooms.Margin = new Padding(10);
            dataGridViewRooms.Name = "dataGridViewRooms";
            dataGridViewRooms.RowHeadersWidth = 51;
            dataGridViewRooms.Size = new Size(844, 402);
            dataGridViewRooms.TabIndex = 2;
            // 
            // panel3
            // 
            panel3.BackColor = Color.Lavender;
            panel3.Controls.Add(lblEmpty);
            panel3.Controls.Add(dataGridViewRooms);
            panel3.Dock = DockStyle.Fill;
            panel3.Location = new Point(0, 79);
            panel3.Margin = new Padding(10);
            panel3.Name = "panel3";
            panel3.Padding = new Padding(10);
            panel3.Size = new Size(875, 441);
            panel3.TabIndex = 6;
            // 
            // RoomForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(panel3);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "RoomForm";
            StartPosition = FormStartPosition.Manual;
            Text = "RoomForm";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewRooms).EndInit();
            panel3.ResumeLayout(false);
            panel3.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label label3;
        private Label lblEmpty;
        private DataGridView dataGridViewRooms;
        private Button btnNewRoom;
        private Label label2;
        private TextBox tbSearch;
        private Panel panel3;
    }
}